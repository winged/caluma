from collections import namedtuple
from typing import Any

FieldInfo = namedtuple('FieldResult', ['pk', 'fields', 'forward_relations', 'reverse_relations', 'fields_and_pk', 'relations'])

RelationInfo = namedtuple('RelationInfo', ['model_field', 'related_model', 'to_many', 'to_field', 'has_through_model', 'reverse'])

def get_field_info(model: Any): ...
def is_abstract_model(model: Any): ...
