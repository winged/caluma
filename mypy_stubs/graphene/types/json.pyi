from .scalars import Scalar as Scalar
from typing import Any

class JSONString(Scalar):
    @staticmethod
    def serialize(dt: Any): ...
    @staticmethod
    def parse_literal(node: Any): ...
    @staticmethod
    def parse_value(value: Any): ...
