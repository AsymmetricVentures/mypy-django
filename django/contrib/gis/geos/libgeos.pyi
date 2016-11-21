# Stubs for django.contrib.gis.geos.libgeos (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from ctypes import Structure

logger = ...  # type: Any

def load_geos(): ...

NOTICEFUNC = ...  # type: Any

def notice_h(fmt, lst): ...

notice_h = ...  # type: Any
ERRORFUNC = ...  # type: Any

def error_h(fmt, lst): ...

error_h = ...  # type: Any

class GEOSGeom_t(Structure): ...
class GEOSPrepGeom_t(Structure): ...
class GEOSCoordSeq_t(Structure): ...
class GEOSContextHandle_t(Structure): ...

GEOM_PTR = ...  # type: Any
PREPGEOM_PTR = ...  # type: Any
CS_PTR = ...  # type: Any
CONTEXT_PTR = ...  # type: Any

def get_pointer_arr(n): ...

lgeos = ...  # type: Any

class GEOSFuncFactory:
    argtypes = ...  # type: Any
    restype = ...  # type: Any
    errcheck = ...  # type: Any
    func_name = ...  # type: Any
    args = ...  # type: Any
    kwargs = ...  # type: Any
    func = ...  # type: Any
    def __init__(self, func_name, *args, **kwargs) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def get_func(self, *args, **kwargs): ...

geos_version = ...  # type: Any
version_regex = ...  # type: Any

def geos_version_info(): ...
