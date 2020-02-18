from .scalars import Scalar as Scalar
from typing import Any

class Date(Scalar):
    @staticmethod
    def serialize(date: Any): ...
    @classmethod
    def parse_literal(cls, node: Any): ...
    @staticmethod
    def parse_value(value: Any): ...

class DateTime(Scalar):
    @staticmethod
    def serialize(dt: Any): ...
    @classmethod
    def parse_literal(cls, node: Any): ...
    @staticmethod
    def parse_value(value: Any): ...

class Time(Scalar):
    @staticmethod
    def serialize(time: Any): ...
    @classmethod
    def parse_literal(cls, node: Any): ...
    @classmethod
    def parse_value(cls, value: Any): ...
