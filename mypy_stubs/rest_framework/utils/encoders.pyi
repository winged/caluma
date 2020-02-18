import json
from rest_framework.compat import coreapi as coreapi
from typing import Any

class JSONEncoder(json.JSONEncoder):
    def default(self, obj: Any): ...
