# Stubs for django.contrib.gis.geos.prototypes.threadsafe (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import threading

class GEOSContextHandle:
    ptr = ...  # type: Any
    def __init__(self) -> None: ...
    def __del__(self): ...

class GEOSContext(threading.local):
    handle = ...  # type: Any

thread_context = ...  # type: Any

class GEOSFunc:
    cfunc = ...  # type: Any
    threaded = ...  # type: bool
    thread_context = ...  # type: Any
    def __init__(self, func_name) -> None: ...
    def __call__(self, *args): ...
    argtypes = ...  # type: Any
    restype = ...  # type: Any
    errcheck = ...  # type: Any