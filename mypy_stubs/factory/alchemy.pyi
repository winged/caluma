from . import base as base
from typing import Any

SESSION_PERSISTENCE_COMMIT: str
SESSION_PERSISTENCE_FLUSH: str
VALID_SESSION_PERSISTENCE_TYPES: Any

class SQLAlchemyOptions(base.FactoryOptions): ...

class SQLAlchemyModelFactory(base.Factory):
    class Meta:
        abstract: bool = ...
