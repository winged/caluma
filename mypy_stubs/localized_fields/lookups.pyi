from django.contrib.postgres.lookups import SearchLookup, TrigramSimilar, Unaccent
from django.db.models.lookups import Contains, EndsWith, Exact, IContains, IEndsWith, IExact, IRegex, IStartsWith, In, IsNull, Regex, StartsWith
from typing import Any

class LocalizedLookupMixin:
    lhs: Any = ...
    def process_lhs(self, qn: Any, connection: Any): ...
    def get_prep_lookup(self): ...

class LocalizedSearchLookup(LocalizedLookupMixin, SearchLookup): ...
class LocalizedUnaccent(LocalizedLookupMixin, Unaccent): ...
class LocalizedTrigramSimilair(LocalizedLookupMixin, TrigramSimilar): ...
class LocalizedExact(LocalizedLookupMixin, Exact): ...
class LocalizedIExact(LocalizedLookupMixin, IExact): ...
class LocalizedIn(LocalizedLookupMixin, In): ...
class LocalizedContains(LocalizedLookupMixin, Contains): ...
class LocalizedIContains(LocalizedLookupMixin, IContains): ...
class LocalizedStartsWith(LocalizedLookupMixin, StartsWith): ...
class LocalizedIStartsWith(LocalizedLookupMixin, IStartsWith): ...
class LocalizedEndsWith(LocalizedLookupMixin, EndsWith): ...
class LocalizedIEndsWith(LocalizedLookupMixin, IEndsWith): ...
class LocalizedIsNullWith(LocalizedLookupMixin, IsNull): ...
class LocalizedRegexWith(LocalizedLookupMixin, Regex): ...
class LocalizedIRegexWith(LocalizedLookupMixin, IRegex): ...
