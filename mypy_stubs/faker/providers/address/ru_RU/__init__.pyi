from .. import Provider as AddressProvider
from typing import Any

class Provider(AddressProvider):
    street_suffixes: Any = ...
    city_formats: Any = ...
    street_name_formats: Any = ...
    street_address_formats: Any = ...
    address_formats: Any = ...
    postcode_formats: Any = ...
    city_prefixes: Any = ...
    street_titles: Any = ...
    city_names: Any = ...
    def city_prefix(self): ...
    def city_name(self): ...
    def street_title(self): ...
