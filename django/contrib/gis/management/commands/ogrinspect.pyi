# Stubs for django.contrib.gis.management.commands.ogrinspect (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import argparse
from django.core.management.base import BaseCommand

class LayerOptionAction(argparse.Action):
    def __call__(self, parser, namespace, value, option_string: Optional[Any] = ...): ...

class ListOptionAction(argparse.Action):
    def __call__(self, parser, namespace, value, option_string: Optional[Any] = ...): ...

class Command(BaseCommand):
    help = ...  # type: str
    requires_system_checks = ...  # type: bool
    def add_arguments(self, parser): ...
    def handle(self, *args, **options): ...
