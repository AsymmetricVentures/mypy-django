# Stubs for django.core.management.commands.shell (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = ...  # type: str
    requires_system_checks = ...  # type: bool
    shells = ...  # type: Any
    def add_arguments(self, parser): ...
    def ipython(self, options): ...
    def bpython(self, options): ...
    def python(self, options): ...
    def handle(self, **options): ...
