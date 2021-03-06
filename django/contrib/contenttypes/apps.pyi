# Stubs for django.contrib.contenttypes.apps (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from .management import inject_rename_contenttypes_operations as inject_rename_contenttypes_operations, update_contenttypes as update_contenttypes

class ContentTypesConfig(AppConfig):
    name = ...  # type: str
    verbose_name = ...  # type: Any
    def ready(self): ...
