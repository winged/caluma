from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import HTTP_HEADER_ENCODING as HTTP_HEADER_ENCODING, exceptions as exceptions
from typing import Any, Optional

def get_authorization_header(request: Any): ...

class CSRFCheck(CsrfViewMiddleware): ...

class BaseAuthentication:
    def authenticate(self, request: Any) -> None: ...
    def authenticate_header(self, request: Any) -> None: ...

class BasicAuthentication(BaseAuthentication):
    www_authenticate_realm: str = ...
    def authenticate(self, request: Any): ...
    def authenticate_credentials(self, userid: Any, password: Any, request: Optional[Any] = ...): ...
    def authenticate_header(self, request: Any): ...

class SessionAuthentication(BaseAuthentication):
    def authenticate(self, request: Any): ...
    def enforce_csrf(self, request: Any) -> None: ...

class TokenAuthentication(BaseAuthentication):
    keyword: str = ...
    model: Any = ...
    def get_model(self): ...
    def authenticate(self, request: Any): ...
    def authenticate_credentials(self, key: Any): ...
    def authenticate_header(self, request: Any): ...

class RemoteUserAuthentication(BaseAuthentication):
    header: str = ...
    def authenticate(self, request: Any): ...
