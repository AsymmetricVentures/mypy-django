# Stubs for django.contrib.staticfiles.management.commands.runserver (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.management.commands.runserver import Command as RunserverCommand

class Command(RunserverCommand):
    help = ...  # type: str
    def add_arguments(self, parser): ...
    def get_handler(self, *args, **options): ...
