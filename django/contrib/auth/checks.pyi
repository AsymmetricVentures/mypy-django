# Stubs for django.contrib.auth.checks (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .management import _get_builtin_permissions as _get_builtin_permissions

def check_user_model(app_configs: Optional[Any] = ..., **kwargs): ...
def check_models_permissions(app_configs: Optional[Any] = ..., **kwargs): ...
