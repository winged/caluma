from parsimonious.utils import StrAndRepr as StrAndRepr
from typing import Any, Optional

class ParseError(StrAndRepr, Exception):
    text: Any = ...
    pos: Any = ...
    expr: Any = ...
    def __init__(self, text: Any, pos: int = ..., expr: Optional[Any] = ...) -> None: ...
    def line(self): ...
    def column(self): ...

class IncompleteParseError(ParseError): ...

class VisitationError(Exception):
    original_class: Any = ...
    def __init__(self, exc: Any, exc_class: Any, node: Any) -> None: ...

class BadGrammar(StrAndRepr, Exception): ...

class UndefinedLabel(BadGrammar):
    label: Any = ...
    def __init__(self, label: Any) -> None: ...
