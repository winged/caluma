from faker import Generator as Generator
from faker.config import AVAILABLE_LOCALES as AVAILABLE_LOCALES, DEFAULT_LOCALE as DEFAULT_LOCALE, PROVIDERS as PROVIDERS
from faker.utils.loading import list_module as list_module
from typing import Any, Optional

logger: Any
inREPL: Any

class Factory:
    @classmethod
    def create(cls, locale: Optional[Any] = ..., providers: Optional[Any] = ..., generator: Optional[Any] = ..., includes: Optional[Any] = ..., **config: Any): ...
