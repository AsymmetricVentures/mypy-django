# Stubs for django.core.management.commands.startapp (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.management.templates import TemplateCommand

class Command(TemplateCommand):
    help = ...  # type: str
    missing_args_message = ...  # type: str
    def handle(self, **options): ...
