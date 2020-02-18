from .sql.types import DjangoDebugSQL as DjangoDebugSQL
from graphene import ObjectType
from typing import Any

class DjangoDebug(ObjectType):
    class Meta:
        description: str = ...
    sql: Any = ...
