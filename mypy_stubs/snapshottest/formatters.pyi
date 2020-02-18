from .generic_repr import GenericRepr as GenericRepr
from .sorted_dict import SortedDict as SortedDict
from typing import Any

class BaseFormatter:
    def can_format(self, value: Any) -> None: ...
    def format(self, value: Any, indent: Any, formatter: Any) -> None: ...
    def get_imports(self): ...
    def assert_value_matches_snapshot(self, test: Any, test_value: Any, snapshot_value: Any, formatter: Any) -> None: ...
    def store(self, test: Any, value: Any): ...
    def normalize(self, value: Any, formatter: Any): ...

class TypeFormatter(BaseFormatter):
    types: Any = ...
    format_func: Any = ...
    def __init__(self, types: Any, format_func: Any) -> None: ...
    def can_format(self, value: Any): ...
    def format(self, value: Any, indent: Any, formatter: Any): ...

class CollectionFormatter(TypeFormatter):
    def normalize(self, value: Any, formatter: Any): ...

class DefaultDictFormatter(TypeFormatter):
    def normalize(self, value: Any, formatter: Any): ...

def trepr(s: Any): ...
def format_none(value: Any, indent: Any, formatter: Any): ...
def format_str(value: Any, indent: Any, formatter: Any): ...
def format_std_type(value: Any, indent: Any, formatter: Any): ...
def format_dict(value: Any, indent: Any, formatter: Any): ...
def format_list(value: Any, indent: Any, formatter: Any): ...
def format_sequence(value: Any, indent: Any, formatter: Any): ...
def format_tuple(value: Any, indent: Any, formatter: Any): ...
def format_set(value: Any, indent: Any, formatter: Any): ...
def format_frozenset(value: Any, indent: Any, formatter: Any): ...

class GenericFormatter(BaseFormatter):
    def can_format(self, value: Any): ...
    def store(self, test: Any, value: Any): ...
    def normalize(self, value: Any, formatter: Any): ...
    def format(self, value: Any, indent: Any, formatter: Any): ...
    def get_imports(self): ...
    def assert_value_matches_snapshot(self, test: Any, test_value: Any, snapshot_value: Any, formatter: Any) -> None: ...

def default_formatters(): ...
