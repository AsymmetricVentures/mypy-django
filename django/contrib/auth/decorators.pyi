# Stubs for django.contrib.auth.decorators (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def user_passes_test(test_func, login_url: Optional[Any] = ..., redirect_field_name: Any = ...): ...
def login_required(function: Optional[Any] = ..., redirect_field_name: Any = ..., login_url: Optional[Any] = ...): ...
def permission_required(perm, login_url: Optional[Any] = ..., raise_exception: bool = ...): ...
