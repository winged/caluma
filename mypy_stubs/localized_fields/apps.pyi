from . import lookups as lookups
from .fields import LocalizedField as LocalizedField
from .lookups import LocalizedLookupMixin as LocalizedLookupMixin
from django.apps import AppConfig

class LocalizedFieldsConfig(AppConfig):
    name: str = ...
    def ready(self) -> None: ...
