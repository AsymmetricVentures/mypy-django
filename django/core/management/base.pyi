# Stubs for django.core.management.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from argparse import ArgumentParser

class CommandError(Exception): ...
class SystemCheckError(CommandError): ...

class CommandParser(ArgumentParser):
    cmd = ...  # type: Any
    def __init__(self, cmd, **kwargs) -> None: ...
    def parse_args(self, args: Optional[Any] = ..., namespace: Optional[Any] = ...): ...
    def error(self, message): ...

def handle_default_options(options): ...

class OutputWrapper:
    @property
    def style_func(self): ...
    @style_func.setter
    def style_func(self, style_func): ...
    style_func = ...  # type: Any
    ending = ...  # type: Any
    def __init__(self, out, style_func: Optional[Any] = ..., ending: str = ...) -> None: ...
    def __getattr__(self, name): ...
    def isatty(self): ...
    def write(self, msg, style_func: Optional[Any] = ..., ending: Optional[Any] = ...): ...

class BaseCommand:
    help = ...  # type: str
    can_import_settings = ...  # type: bool
    output_transaction = ...  # type: bool
    leave_locale_alone = ...  # type: bool
    requires_migrations_checks = ...  # type: bool
    requires_system_checks = ...  # type: bool
    stdout = ...  # type: Any
    stderr = ...  # type: Any
    style = ...  # type: Any
    def __init__(self, stdout: Optional[Any] = ..., stderr: Optional[Any] = ..., no_color: bool = ...) -> None: ...
    def get_version(self): ...
    def create_parser(self, prog_name, subcommand): ...
    def add_arguments(self, parser): ...
    def print_help(self, prog_name, subcommand): ...
    def run_from_argv(self, argv): ...
    def execute(self, *args, **options): ...
    def check(self, app_configs: Optional[Any] = ..., tags: Optional[Any] = ..., display_num_errors: bool = ..., include_deployment_checks: bool = ..., fail_level: Any = ...): ...
    def check_migrations(self): ...
    def handle(self, *args, **options): ...

class AppCommand(BaseCommand):
    missing_args_message = ...  # type: str
    def add_arguments(self, parser): ...
    def handle(self, *app_labels, **options): ...
    def handle_app_config(self, app_config, **options): ...

class LabelCommand(BaseCommand):
    label = ...  # type: str
    missing_args_message = ...  # type: Any
    def add_arguments(self, parser): ...
    def handle(self, *labels, **options): ...
    def handle_label(self, label, **options): ...
