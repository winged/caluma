from rest_framework.settings import api_settings as api_settings
from rest_framework.utils.urls import replace_query_param as replace_query_param
from typing import Any, Optional

def preserve_builtin_query_params(url: Any, request: Optional[Any] = ...): ...
def reverse(viewname: Any, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., request: Optional[Any] = ..., format: Optional[Any] = ..., **extra: Any): ...

reverse_lazy: Any
