# Stubs for django.core.cache.backends.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.core.exceptions import DjangoRuntimeWarning, ImproperlyConfigured

class InvalidCacheBackendError(ImproperlyConfigured): ...
class CacheKeyWarning(DjangoRuntimeWarning): ...

DEFAULT_TIMEOUT = ...  # type: Any
MEMCACHE_MAX_KEY_LENGTH = ...  # type: int

def default_key_func(key, key_prefix, version): ...
def get_key_func(key_func): ...

class BaseCache:
    default_timeout = ...  # type: Any
    key_prefix = ...  # type: Any
    version = ...  # type: Any
    key_func = ...  # type: Any
    def __init__(self, params) -> None: ...
    def get_backend_timeout(self, timeout: Any = ...): ...
    def make_key(self, key, version: Optional[Any] = ...): ...
    def add(self, key, value, timeout: Any = ..., version: Optional[Any] = ...): ...
    def get(self, key, default: Optional[Any] = ..., version: Optional[Any] = ...): ...
    def set(self, key, value, timeout: Any = ..., version: Optional[Any] = ...): ...
    def delete(self, key, version: Optional[Any] = ...): ...
    def get_many(self, keys, version: Optional[Any] = ...): ...
    def get_or_set(self, key, default: Optional[Any] = ..., timeout: Any = ..., version: Optional[Any] = ...): ...
    def has_key(self, key, version: Optional[Any] = ...): ...
    def incr(self, key, delta: int = ..., version: Optional[Any] = ...): ...
    def decr(self, key, delta: int = ..., version: Optional[Any] = ...): ...
    def __contains__(self, key): ...
    def set_many(self, data, timeout: Any = ..., version: Optional[Any] = ...): ...
    def delete_many(self, keys, version: Optional[Any] = ...): ...
    def clear(self): ...
    def validate_key(self, key): ...
    def incr_version(self, key, delta: int = ..., version: Optional[Any] = ...): ...
    def decr_version(self, key, delta: int = ..., version: Optional[Any] = ...): ...
    def close(self, **kwargs): ...
