from typing import Any

is_init_subclass_available: Any

class InitSubclassMeta(type):
    def __new__(cls, name: Any, bases: Any, ns: Any, **kwargs: Any): ...
    def __init__(cls, name: Any, bases: Any, ns: Any, **kwargs: Any) -> None: ...
InitSubclassMeta = type
