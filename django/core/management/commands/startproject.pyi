# Stubs for django.core.management.commands.startproject (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.management.templates import TemplateCommand
from ..utils import get_random_secret_key as get_random_secret_key

class Command(TemplateCommand):
    help = ...  # type: str
    missing_args_message = ...  # type: str
    def handle(self, **options): ...
