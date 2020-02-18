from ..forms import LocalizedCharFieldForm as LocalizedCharFieldForm
from ..value import LocalizedStringValue as LocalizedStringValue
from .field import LocalizedField as LocalizedField
from typing import Any

class LocalizedCharField(LocalizedField):
    attr_class: Any = ...
    def formfield(self, **kwargs: Any): ...
