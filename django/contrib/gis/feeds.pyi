# Stubs for django.contrib.gis.feeds (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.contrib.syndication.views import Feed as BaseFeed
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed

class GeoFeedMixin:
    def georss_coords(self, coords): ...
    def add_georss_point(self, handler, coords, w3c_geo: bool = ...): ...
    def add_georss_element(self, handler, item, w3c_geo: bool = ...): ...

class GeoRSSFeed(Rss201rev2Feed, GeoFeedMixin):
    def rss_attributes(self): ...
    def add_item_elements(self, handler, item): ...
    def add_root_elements(self, handler): ...

class GeoAtom1Feed(Atom1Feed, GeoFeedMixin):
    def root_attributes(self): ...
    def add_item_elements(self, handler, item): ...
    def add_root_elements(self, handler): ...

class W3CGeoFeed(Rss201rev2Feed, GeoFeedMixin):
    def rss_attributes(self): ...
    def add_item_elements(self, handler, item): ...
    def add_root_elements(self, handler): ...

class Feed(BaseFeed):
    feed_type = ...  # type: Any
    def feed_extra_kwargs(self, obj): ...
    def item_extra_kwargs(self, item): ...
