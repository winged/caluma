import threading
from concurrent.futures import ThreadPoolExecutor

import pytest
from django.db import close_old_connections
from graphql_relay import to_global_id

from caluma.caluma_form import api, domain_logic, models
from caluma.caluma_form.api import save_answer
from caluma.caluma_form.models import Answer
from caluma.caluma_form.validators import AnswerValidator


def test_save_answer_with_context(db, mocker, question_factory, document):
    mocker.patch.object(AnswerValidator, "validate")

    question = question_factory(type="text")
    save_answer(question, document, value="foo", context={"bar": "baz"})

    answer = Answer.objects.first()
    assert answer.value == "foo"

    AnswerValidator.validate.assert_called_once_with(
        data_source_context={"bar": "baz"},
        document=document,
        instance=None,
        origin=True,
        question=question,
        user=None,
        value="foo",
    )


@pytest.mark.parametrize("question__type", [models.Question.TYPE_TEXT])
def test_save_answer_via_graphql_locks_family(db, mocker, answer, schema_executor):
    lock_family = mocker.spy(api, "_lock_family")
    validate_for_save = mocker.spy(domain_logic.SaveAnswerLogic, "validate_for_save")
    query = """
        mutation saveDocumentStringAnswer($input: SaveDocumentStringAnswerInput!) {
          saveDocumentStringAnswer(input: $input) {
            answer {
              ... on StringAnswer {
                value
              }
            }
          }
        }
    """
    variables = {
        "input": {
            "document": to_global_id("StringAnswer", answer.document.pk),
            "question": to_global_id("StringAnswer", answer.question.pk),
            "value": "updated",
        }
    }

    result = schema_executor(query, variable_values=variables)

    assert not result.errors
    assert result.data["saveDocumentStringAnswer"]["answer"]["value"] == "updated"
    lock_family.assert_called_once_with(answer.document)
    validate_for_save.assert_called_once()


def test_save_document_via_graphql_locks_family(db, mocker, document, schema_executor):
    lock_family = mocker.spy(api, "_lock_family")
    document.meta = {"existing": "value"}
    document.save()
    query = """
        mutation saveDocument($input: SaveDocumentInput!) {
          saveDocument(input: $input) {
            document {
              id
            }
          }
        }
    """
    variables = {
        "input": {
            "id": str(document.pk),
            "form": document.form.pk,
        }
    }

    result = schema_executor(query, variable_values=variables)

    assert not result.errors
    document.refresh_from_db()
    assert document.meta == {"existing": "value"}
    lock_family.assert_called_once_with(document)


def test_remove_answer_via_graphql_locks_family(db, mocker, answer, schema_executor):
    lock_family = mocker.spy(api, "_lock_family")
    query = """
        mutation removeAnswer($input: RemoveAnswerInput!) {
          removeAnswer(input: $input) {
            clientMutationId
          }
        }
    """

    result = schema_executor(
        query, variable_values={"input": {"answer": str(answer.pk)}}
    )

    assert not result.errors
    lock_family.assert_called_once_with(answer.document)


def test_remove_document_via_graphql_locks_family(
    db, mocker, document, schema_executor
):
    lock_family = mocker.spy(api, "_lock_family")
    query = """
        mutation removeDocument($input: RemoveDocumentInput!) {
          removeDocument(input: $input) {
            clientMutationId
          }
        }
    """

    result = schema_executor(
        query, variable_values={"input": {"document": str(document.pk)}}
    )

    assert not result.errors
    assert lock_family.call_count == 1
    assert lock_family.call_args.args[0].family_id == document.family_id


def test_save_answer_serializes_document_family_updates(
    transactional_db,
    mocker,
    form_factory,
    form_question_factory,
    document_factory,
):
    """
    Verify concurrent updates in one document family serialize before recalculation.

    Without serialization, each update could recalculate dependent answers without
    seeing the other update and overwrite them with a stale result. The family lock
    ensures each recalculation sees updates committed by the preceding save.
    """

    form = form_factory()
    question_a = form_question_factory(
        form=form,
        question__slug="input-a",
        question__type=models.Question.TYPE_INTEGER,
    ).question
    question_b = form_question_factory(
        form=form,
        question__slug="input-b",
        question__type=models.Question.TYPE_INTEGER,
    ).question
    calculated_question = form_question_factory(
        form=form,
        question__type=models.Question.TYPE_CALCULATED_FLOAT,
        question__calc_expression="'input-a'|answer + 'input-b'|answer",
    ).question
    document = document_factory(form=form)

    save_answer(question_a, document, value=0)
    save_answer(question_b, document, value=0)
    question_a.refresh_from_db()
    question_b.refresh_from_db()

    # A barrier pauses each thread until both have reached recalculation. Without
    # the family lock, this forces both saves to recalculate from concurrent data.
    recalculation_barrier = threading.Barrier(2)
    recalculate_dependent_fields = domain_logic.recalculate_dependent_fields

    def synchronize_recalculation(field):
        try:
            recalculation_barrier.wait(timeout=1)
        except threading.BrokenBarrierError:
            # With the family lock, the second save cannot arrive before timeout.
            pass
        recalculate_dependent_fields(field)

    mocker.patch.object(
        domain_logic,
        "recalculate_dependent_fields",
        side_effect=synchronize_recalculation,
    )

    def update_answer(question, value):
        # Give each worker thread its own database connection and transaction.
        close_old_connections()
        try:
            save_answer(question, document, value=value)
        finally:
            close_old_connections()

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [
            executor.submit(update_answer, question_a, 1),
            executor.submit(update_answer, question_b, 2),
        ]
        for future in futures:
            future.result(timeout=5)

    calculated_answer = Answer.objects.get(
        question=calculated_question, document=document
    )
    assert calculated_answer.value == 3
