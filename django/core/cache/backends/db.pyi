# Stubs for django.core.cache.backends.db (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.core.cache.backends.base import BaseCache
from django.utils.six.moves import cPickle as pickle

class Options:
    db_table = ...  # type: Any
    app_label = ...  # type: str
    model_name = ...  # type: str
    verbose_name = ...  # type: str
    verbose_name_plural = ...  # type: str
    object_name = ...  # type: str
    abstract = ...  # type: bool
    managed = ...  # type: bool
    proxy = ...  # type: bool
    swapped = ...  # type: bool
    def __init__(self, table) -> None: ...

class BaseDatabaseCache(BaseCache):
    cache_model_class = ...  # type: Any
    def __init__(self, table, params) -> None: ...

class DatabaseCache(BaseDatabaseCache):
    def get(self, key, default: Optional[Any] = ..., version: Optional[Any] = ...): ...
    def set(self, key, value, timeout: Any = ..., version: Optional[Any] = ...): ...
    def add(self, key, value, timeout: Any = ..., version: Optional[Any] = ...): ...
    def delete(self, key, version: Optional[Any] = ...): ...
    def has_key(self, key, version: Optional[Any] = ...): ...
    def clear(self): ...
