from .. import Provider as AutomotiveProvider
from typing import Any

class Provider(AutomotiveProvider):
    license_plate_letters: Any = ...
    license_plate_suffix: Any = ...
    license_plate_number: str = ...
    def license_plate(self): ...
