from rest_framework.exceptions import ValidationError as ValidationError
from rest_framework.utils.representation import smart_repr as smart_repr
from typing import Any, Optional

def qs_exists(queryset: Any): ...
def qs_filter(queryset: Any, **kwargs: Any): ...

class UniqueValidator:
    message: Any = ...
    queryset: Any = ...
    serializer_field: Any = ...
    lookup: Any = ...
    def __init__(self, queryset: Any, message: Optional[Any] = ..., lookup: str = ...) -> None: ...
    field_name: Any = ...
    instance: Any = ...
    def set_context(self, serializer_field: Any) -> None: ...
    def filter_queryset(self, value: Any, queryset: Any): ...
    def exclude_current_instance(self, queryset: Any): ...
    def __call__(self, value: Any) -> None: ...

class UniqueTogetherValidator:
    message: Any = ...
    missing_message: Any = ...
    queryset: Any = ...
    fields: Any = ...
    serializer_field: Any = ...
    def __init__(self, queryset: Any, fields: Any, message: Optional[Any] = ...) -> None: ...
    instance: Any = ...
    def set_context(self, serializer: Any) -> None: ...
    def enforce_required_fields(self, attrs: Any) -> None: ...
    def filter_queryset(self, attrs: Any, queryset: Any): ...
    def exclude_current_instance(self, attrs: Any, queryset: Any): ...
    def __call__(self, attrs: Any) -> None: ...

class BaseUniqueForValidator:
    message: Any = ...
    missing_message: Any = ...
    queryset: Any = ...
    field: Any = ...
    date_field: Any = ...
    def __init__(self, queryset: Any, field: Any, date_field: Any, message: Optional[Any] = ...) -> None: ...
    field_name: Any = ...
    date_field_name: Any = ...
    instance: Any = ...
    def set_context(self, serializer: Any) -> None: ...
    def enforce_required_fields(self, attrs: Any) -> None: ...
    def filter_queryset(self, attrs: Any, queryset: Any) -> None: ...
    def exclude_current_instance(self, attrs: Any, queryset: Any): ...
    def __call__(self, attrs: Any) -> None: ...

class UniqueForDateValidator(BaseUniqueForValidator):
    message: Any = ...
    def filter_queryset(self, attrs: Any, queryset: Any): ...

class UniqueForMonthValidator(BaseUniqueForValidator):
    message: Any = ...
    def filter_queryset(self, attrs: Any, queryset: Any): ...

class UniqueForYearValidator(BaseUniqueForValidator):
    message: Any = ...
    def filter_queryset(self, attrs: Any, queryset: Any): ...
