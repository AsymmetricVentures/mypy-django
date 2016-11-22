# Stubs for django.contrib.sites.managers (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.db import models

class CurrentSiteManager(models.Manager):
    use_in_migrations = ...  # type: bool
    def __init__(self, field_name: Optional[Any] = ...) -> None: ...
    def check(self, **kwargs): ...
    def get_queryset(self): ...
