from django.core.exceptions import FieldError
from typing import Any

class FieldLookupError(FieldError):
    def __init__(self, model_field: Any, lookup_expr: Any) -> None: ...
