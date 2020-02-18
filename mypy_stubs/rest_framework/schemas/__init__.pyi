from . import coreapi as coreapi, openapi as openapi
from .coreapi import AutoSchema as AutoSchema, ManualSchema as ManualSchema, SchemaGenerator as SchemaGenerator
from .inspectors import DefaultSchema as DefaultSchema
from rest_framework.settings import api_settings as api_settings
from typing import Any, Optional

def get_schema_view(title: Optional[Any] = ..., url: Optional[Any] = ..., description: Optional[Any] = ..., urlconf: Optional[Any] = ..., renderer_classes: Optional[Any] = ..., public: bool = ..., patterns: Optional[Any] = ..., generator_class: Optional[Any] = ..., authentication_classes: Any = ..., permission_classes: Any = ..., version: Optional[Any] = ...): ...
