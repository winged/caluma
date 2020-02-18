from .compat import getargspec as getargspec
from faker import utils as utils
from typing import Any, Optional

class Documentor:
    generator: Any = ...
    max_name_len: int = ...
    already_generated: Any = ...
    def __init__(self, generator: Any) -> None: ...
    def get_formatters(self, locale: Optional[Any] = ..., excludes: Optional[Any] = ..., **kwargs: Any): ...
    def get_provider_formatters(self, provider: Any, prefix: str = ..., with_args: bool = ..., with_defaults: bool = ...): ...
    @staticmethod
    def get_provider_name(provider_class: Any): ...
