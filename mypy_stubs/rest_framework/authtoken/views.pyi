from rest_framework import parsers as parsers, renderers as renderers
from rest_framework.authtoken.models import Token as Token
from rest_framework.authtoken.serializers import AuthTokenSerializer as AuthTokenSerializer
from rest_framework.compat import coreapi as coreapi, coreschema as coreschema
from rest_framework.response import Response as Response
from rest_framework.schemas import ManualSchema as ManualSchema
from rest_framework.views import APIView as APIView
from typing import Any

class ObtainAuthToken(APIView):
    throttle_classes: Any = ...
    permission_classes: Any = ...
    parser_classes: Any = ...
    renderer_classes: Any = ...
    serializer_class: Any = ...
    schema: Any = ...
    def post(self, request: Any, *args: Any, **kwargs: Any): ...

obtain_auth_token: Any
