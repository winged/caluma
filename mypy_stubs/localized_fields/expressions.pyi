from psqlextra import expressions
from typing import Any

class LocalizedRef(expressions.HStoreRef):
    def __init__(self, name: str, lang: str=...) -> Any: ...
