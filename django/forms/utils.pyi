# Stubs for django.forms.utils (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.utils.translation import ugettext_lazy as _
from collections import UserList
from UserList import UserList

def pretty_name(name): ...
def flatatt(attrs): ...

class ErrorDict(dict):
    def as_data(self): ...
    def as_json(self, escape_html: bool = ...): ...
    def as_ul(self): ...
    def as_text(self): ...

class ErrorList(UserList, list):
    error_class = ...  # type: str
    def __init__(self, initlist: Optional[Any] = ..., error_class: Optional[Any] = ...) -> None: ...
    def as_data(self): ...
    def get_json_data(self, escape_html: bool = ...): ...
    def as_json(self, escape_html: bool = ...): ...
    def as_ul(self): ...
    def as_text(self): ...
    def __contains__(self, item): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __getitem__(self, i): ...
    def __reduce_ex__(self, *args, **kwargs): ...

def from_current_timezone(value): ...
def to_current_timezone(value): ...
