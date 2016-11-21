# Stubs for django.contrib.syndication.views (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.core.exceptions import ObjectDoesNotExist

def add_domain(domain, url, secure: bool = ...): ...

class FeedDoesNotExist(ObjectDoesNotExist): ...

class Feed:
    feed_type = ...  # type: Any
    title_template = ...  # type: Any
    description_template = ...  # type: Any
    def __call__(self, request, *args, **kwargs): ...
    def item_title(self, item): ...
    def item_description(self, item): ...
    def item_link(self, item): ...
    def item_enclosures(self, item): ...
    def feed_extra_kwargs(self, obj): ...
    def item_extra_kwargs(self, item): ...
    def get_object(self, request, *args, **kwargs): ...
    def get_context_data(self, **kwargs): ...
    def get_feed(self, obj, request): ...
