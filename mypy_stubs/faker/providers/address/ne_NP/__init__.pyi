from .. import Provider as AddressProvider
from typing import Any

class Provider(AddressProvider):
    building_number_formats: Any = ...
    street_name_formats: Any = ...
    street_address_formats: Any = ...
    city_formats: Any = ...
    postcode_formats: Any = ...
    address_formats: Any = ...
    street_suffixes: Any = ...
    building_prefixes: Any = ...
    countries: Any = ...
    cities: Any = ...
    districts: Any = ...
    def district(self): ...
    def city(self): ...
    def building_prefix(self): ...
