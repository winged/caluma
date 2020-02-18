from .. import compat as compat
from .filters import BooleanFilter as BooleanFilter, IsoDateTimeFilter as IsoDateTimeFilter
from django_filters import filterset as filterset
from typing import Any

FILTER_FOR_DBFIELD_DEFAULTS: Any

class FilterSet(filterset.FilterSet):
    FILTER_DEFAULTS: Any = ...
    @property
    def form(self): ...
