# Stubs for django.contrib.gis.geos.point (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.contrib.gis.geos import prototypes as capi
from django.contrib.gis.geos.geometry import GEOSGeometry

class Point(GEOSGeometry):
    has_cs = ...  # type: bool
    def __init__(self, x: Optional[Any] = ..., y: Optional[Any] = ..., z: Optional[Any] = ..., srid: Optional[Any] = ...) -> None: ...
    def __iter__(self): ...
    def __len__(self): ...
    @property
    def x(self): ...
    @x.setter
    def x(self, value): ...
    @property
    def y(self): ...
    @y.setter
    def y(self, value): ...
    @property
    def z(self): ...
    @z.setter
    def z(self, value): ...
    def get_x(self): ...
    x = ...  # type: Any
    def set_x(self, value): ...
    def get_y(self): ...
    y = ...  # type: Any
    def set_y(self, value): ...
    def get_z(self): ...
    z = ...  # type: Any
    def set_z(self, value): ...
    @property
    def tuple(self): ...
    @tuple.setter
    def tuple(self, tup): ...
    def get_coords(self): ...
    tuple = ...  # type: Any
    def set_coords(self, tup): ...
    coords = ...  # type: Any
