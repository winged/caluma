from .. import BaseProvider as BaseProvider
from typing import Any

class Provider(BaseProvider):
    jobs: Any = ...
    def job(self): ...
