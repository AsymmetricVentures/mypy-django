# Stubs for django.contrib.gis.db.backends.base.models (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class SpatialRefSysMixin:
    spheroid_regex = ...  # type: Any
    units_regex = ...  # type: Any
    @property
    def srs(self): ...
    @property
    def ellipsoid(self): ...
    @property
    def name(self): ...
    @property
    def spheroid(self): ...
    @property
    def datum(self): ...
    @property
    def projected(self): ...
    @property
    def local(self): ...
    @property
    def geographic(self): ...
    @property
    def linear_name(self): ...
    @property
    def linear_units(self): ...
    @property
    def angular_name(self): ...
    @property
    def angular_units(self): ...
    @property
    def units(self): ...
    @classmethod
    def get_units(cls, wkt): ...
    @classmethod
    def get_spheroid(cls, wkt, string: bool = ...): ...
