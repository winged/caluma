from .base import BaseOptions as BaseOptions, BaseType as BaseType
from .field import Field as Field
from .utils import yank_fields_from_attrs as yank_fields_from_attrs
from typing import Any, Dict, Optional

MYPY: bool

class InterfaceOptions(BaseOptions):
    fields: Dict[str, Field] = ...

class Interface(BaseType):
    @classmethod
    def __init_subclass_with_meta__(cls, _meta: Optional[Any] = ..., **options: Any) -> None: ...
    @classmethod
    def resolve_type(cls, instance: Any, info: Any): ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
