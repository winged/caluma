from .scalars import Scalar as Scalar
from typing import Any

class UUID(Scalar):
    @staticmethod
    def serialize(uuid: Any): ...
    @staticmethod
    def parse_literal(node: Any): ...
    @staticmethod
    def parse_value(value: Any): ...
