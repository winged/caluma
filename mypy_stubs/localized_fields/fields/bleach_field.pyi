from .field import LocalizedField as LocalizedField
from typing import Any

class LocalizedBleachField(LocalizedField):
    def pre_save(self, instance: Any, add: bool) -> Any: ...
