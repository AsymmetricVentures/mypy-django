# Stubs for django.contrib.gis.geos.prepared (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .base import GEOSBase as GEOSBase
from .prototypes import prepared as capi

class PreparedGeometry(GEOSBase):
    ptr_type = ...  # type: Any
    ptr = ...  # type: Any
    def __init__(self, geom) -> None: ...
    def __del__(self): ...
    def contains(self, other): ...
    def contains_properly(self, other): ...
    def covers(self, other): ...
    def intersects(self, other): ...
    def crosses(self, other): ...
    def disjoint(self, other): ...
    def overlaps(self, other): ...
    def touches(self, other): ...
    def within(self, other): ...