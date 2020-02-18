from rest_framework import HTTP_HEADER_ENCODING as HTTP_HEADER_ENCODING, exceptions as exceptions
from rest_framework.settings import api_settings as api_settings
from rest_framework.utils.mediatypes import media_type_matches as media_type_matches, order_by_precedence as order_by_precedence
from typing import Any, Optional

class BaseContentNegotiation:
    def select_parser(self, request: Any, parsers: Any) -> None: ...
    def select_renderer(self, request: Any, renderers: Any, format_suffix: Optional[Any] = ...) -> None: ...

class DefaultContentNegotiation(BaseContentNegotiation):
    settings: Any = ...
    def select_parser(self, request: Any, parsers: Any): ...
    def select_renderer(self, request: Any, renderers: Any, format_suffix: Optional[Any] = ...): ...
    def filter_renderers(self, renderers: Any, format: Any): ...
    def get_accept_list(self, request: Any): ...
