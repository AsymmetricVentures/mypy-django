# Stubs for django.core.management.commands.sqlflush (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = ...  # type: str
    output_transaction = ...  # type: bool
    def add_arguments(self, parser): ...
    def handle(self, **options): ...
