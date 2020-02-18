from ..mixins import AtomicSlugRetryMixin as AtomicSlugRetryMixin
from ..util import get_language_codes as get_language_codes
from ..value import LocalizedValue as LocalizedValue
from .autoslug_field import LocalizedAutoSlugField as LocalizedAutoSlugField
from typing import Any

class LocalizedUniqueSlugField(LocalizedAutoSlugField):
    populate_from: Any = ...
    include_time: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def deconstruct(self): ...
    def pre_save(self, instance: Any, add: bool) -> Any: ...
