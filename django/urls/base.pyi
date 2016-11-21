# Stubs for django.urls.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .exceptions import NoReverseMatch as NoReverseMatch, Resolver404 as Resolver404
from .resolvers import get_ns_resolver as get_ns_resolver, get_resolver as get_resolver
from .utils import get_callable as get_callable

def resolve(path, urlconf: Optional[Any] = ...): ...
def reverse(viewname, urlconf: Optional[Any] = ..., args: Optional[Any] = ..., kwargs: Optional[Any] = ..., current_app: Optional[Any] = ...): ...

reverse_lazy = ...  # type: Any

def clear_url_caches(): ...
def set_script_prefix(prefix): ...
def get_script_prefix(): ...
def clear_script_prefix(): ...
def set_urlconf(urlconf_name): ...
def get_urlconf(default: Optional[Any] = ...): ...
def is_valid_path(path, urlconf: Optional[Any] = ...): ...
def translate_url(url, lang_code): ...
