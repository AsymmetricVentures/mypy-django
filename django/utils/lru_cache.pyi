# Stubs for django.utils.lru_cache (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from collections import namedtuple

_CacheInfo = namedtuple('CacheInfo', ['hits', 'misses', 'maxsize', 'currsize'])

class _HashedSeq(list):
    hashvalue = ...  # type: Any
    def __init__(self, tup, hash: Any = ...) -> None: ...
    def __hash__(self): ...

def lru_cache(maxsize: int = ..., typed: bool = ...): ...