from .base import BaseOptions as BaseOptions, BaseType as BaseType
from .unmountedtype import UnmountedType as UnmountedType
from typing import Any

class ScalarOptions(BaseOptions): ...

class Scalar(UnmountedType, BaseType):
    @classmethod
    def __init_subclass_with_meta__(cls, **options: Any) -> None: ...
    serialize: Any = ...
    parse_value: Any = ...
    parse_literal: Any = ...
    @classmethod
    def get_type(cls): ...

MAX_INT: int
MIN_INT: int

class Int(Scalar):
    @staticmethod
    def coerce_int(value: Any): ...
    serialize: Any = ...
    parse_value: Any = ...
    @staticmethod
    def parse_literal(ast: Any): ...

class Float(Scalar):
    @staticmethod
    def coerce_float(value: Any) -> float: ...
    serialize: Any = ...
    parse_value: Any = ...
    @staticmethod
    def parse_literal(ast: Any): ...

class String(Scalar):
    @staticmethod
    def coerce_string(value: Any): ...
    serialize: Any = ...
    parse_value: Any = ...
    @staticmethod
    def parse_literal(ast: Any): ...

class Boolean(Scalar):
    serialize: Any = ...
    parse_value: Any = ...
    @staticmethod
    def parse_literal(ast: Any): ...

class ID(Scalar):
    serialize: Any = ...
    parse_value: Any = ...
    @staticmethod
    def parse_literal(ast: Any): ...
