from .. import Provider as AddressProvider
from typing import Any, Optional

class Provider(AddressProvider):
    city_prefixes: Any = ...
    city_suffixes: Any = ...
    street_prefixes: Any = ...
    street_suffixes: Any = ...
    village_prefixes: Any = ...
    address_formats: Any = ...
    building_number_formats: Any = ...
    postcode_formats: Any = ...
    secondary_address_formats: Any = ...
    street_address_formats: Any = ...
    street_name_formats: Any = ...
    cities: Any = ...
    countries: Any = ...
    states: Any = ...
    states_abbr: Any = ...
    states_postcode: Any = ...
    streets: Any = ...
    villages: Any = ...
    def city(self): ...
    def city_prefix(self): ...
    def postcode(self): ...
    def postcode_in_state(self, state_abbr: Optional[Any] = ...): ...
    def secondary_address(self): ...
    def state(self): ...
    def state_abbr(self): ...
    def street(self): ...
    def street_prefix(self): ...
    def village(self): ...
    def village_prefix(self): ...
