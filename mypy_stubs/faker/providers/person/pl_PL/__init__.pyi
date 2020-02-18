from .. import Provider as PersonProvider
from typing import Any, Optional

def checksum_identity_card_number(characters: Any): ...

class Provider(PersonProvider):
    formats: Any = ...
    first_names_male: Any = ...
    first_names_female: Any = ...
    unisex_last_names: Any = ...
    male_last_names: Any = ...
    prefixes_male: Any = ...
    prefixes_female: Any = ...
    first_names: Any = ...
    def last_name(self): ...
    def identity_card_number(self): ...
    @staticmethod
    def pesel_compute_check_digit(pesel: Any): ...
    def pesel(self, date_of_birth: Optional[Any] = ..., sex: Optional[Any] = ...): ...
    @staticmethod
    def pwz_doctor_compute_check_digit(x: Any): ...
    def pwz_doctor(self): ...
    def pwz_nurse(self, kind: str = ...): ...
