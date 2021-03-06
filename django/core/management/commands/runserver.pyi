# Stubs for django.core.management.commands.runserver (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.core.management.base import BaseCommand

naiveip_re = ...  # type: Any

class Command(BaseCommand):
    help = ...  # type: str
    requires_system_checks = ...  # type: bool
    leave_locale_alone = ...  # type: bool
    default_port = ...  # type: str
    def add_arguments(self, parser): ...
    def execute(self, *args, **options): ...
    def get_handler(self, *args, **options): ...
    use_ipv6 = ...  # type: Any
    addr = ...  # type: str
    port = ...  # type: Any
    def handle(self, *args, **options): ...
    def run(self, **options): ...
    def inner_run(self, *args, **options): ...

BaseRunserverCommand = ...  # type: Any
