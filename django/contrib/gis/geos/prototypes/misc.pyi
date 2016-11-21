# Stubs for django.contrib.gis.geos.prototypes.misc (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.contrib.gis.geos.libgeos import GEOSFuncFactory

class DblFromGeom(GEOSFuncFactory):
    restype = ...  # type: Any
    errcheck = ...  # type: Any
    argtypes = ...  # type: Any
    def get_func(self, num_geom: int = ...): ...

geos_area = ...  # type: Any
geos_distance = ...  # type: Any
geos_length = ...  # type: Any
geos_isvalidreason = ...  # type: Any
