from .mixins import AtomicSlugRetryMixin as AtomicSlugRetryMixin
from psqlextra.models import PostgresModel

class LocalizedModel(AtomicSlugRetryMixin, PostgresModel):
    class Meta:
        abstract: bool = ...
