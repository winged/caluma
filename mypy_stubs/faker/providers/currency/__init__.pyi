from .. import BaseProvider as BaseProvider
from typing import Any

class Provider(BaseProvider):
    currencies: Any = ...
    cryptocurrencies: Any = ...
    def currency(self): ...
    def currency_code(self): ...
    def currency_name(self): ...
    def cryptocurrency(self): ...
    def cryptocurrency_code(self): ...
    def cryptocurrency_name(self): ...
