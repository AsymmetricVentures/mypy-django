# Stubs for django.core.management.commands.dumpdata (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.management.base import BaseCommand

class ProxyModelWarning(Warning): ...

class Command(BaseCommand):
    help = ...  # type: str
    def add_arguments(self, parser): ...
    def handle(self, *app_labels, **options): ...
