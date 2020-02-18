from .settings import graphene_settings as graphene_settings
from .utils import maybe_queryset as maybe_queryset
from graphene.relay import ConnectionField
from graphene.types import Field
from typing import Any

class DjangoListField(Field):
    def __init__(self, _type: Any, *args: Any, **kwargs: Any) -> None: ...
    @property
    def model(self): ...
    @staticmethod
    def list_resolver(django_object_type: Any, resolver: Any, root: Any, info: Any, **args: Any): ...
    def get_resolver(self, parent_resolver: Any): ...

class DjangoConnectionField(ConnectionField):
    on: Any = ...
    max_limit: Any = ...
    enforce_first_or_last: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def type(self): ...
    @property
    def connection_type(self): ...
    @property
    def node_type(self): ...
    @property
    def model(self): ...
    def get_manager(self): ...
    @classmethod
    def resolve_queryset(cls, connection: Any, queryset: Any, info: Any, args: Any): ...
    @classmethod
    def resolve_connection(cls, connection: Any, args: Any, iterable: Any): ...
    @classmethod
    def connection_resolver(cls, resolver: Any, connection: Any, default_manager: Any, queryset_resolver: Any, max_limit: Any, enforce_first_or_last: Any, root: Any, info: Any, **args: Any): ...
    def get_resolver(self, parent_resolver: Any): ...
    def get_queryset_resolver(self): ...
