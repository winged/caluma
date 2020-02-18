from .scalars import Scalar as Scalar
from typing import Any

class Decimal(Scalar):
    @staticmethod
    def serialize(dec: Any): ...
    @classmethod
    def parse_literal(cls, node: Any): ...
    @staticmethod
    def parse_value(value: Any): ...
