# Stubs for django.contrib.gis.geos.io (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.contrib.gis.geos.prototypes.io import WKBWriter as WKBWriter, WKTWriter as WKTWriter
from django.contrib.gis.geos.prototypes.io import _WKBReader, _WKTReader

class WKBReader(_WKBReader):
    def read(self, wkb): ...

class WKTReader(_WKTReader):
    def read(self, wkt): ...
