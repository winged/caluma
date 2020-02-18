from ..forms import LocalizedTextFieldForm as LocalizedTextFieldForm
from .char_field import LocalizedCharField as LocalizedCharField
from typing import Any

class LocalizedTextField(LocalizedCharField):
    def formfield(self, **kwargs: Any): ...
