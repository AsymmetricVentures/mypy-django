# Stubs for django.contrib.staticfiles.management.commands.collectstatic (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = ...  # type: str
    requires_system_checks = ...  # type: bool
    copied_files = ...  # type: Any
    symlinked_files = ...  # type: Any
    unmodified_files = ...  # type: Any
    post_processed_files = ...  # type: Any
    storage = ...  # type: Any
    style = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def local(self): ...
    def add_arguments(self, parser): ...
    interactive = ...  # type: Any
    verbosity = ...  # type: Any
    symlink = ...  # type: Any
    clear = ...  # type: Any
    dry_run = ...  # type: Any
    ignore_patterns = ...  # type: Any
    post_process = ...  # type: Any
    def set_options(self, **options): ...
    def collect(self): ...
    def handle(self, **options): ...
    def log(self, msg, level: int = ...): ...
    def is_local_storage(self): ...
    def clear_dir(self, path): ...
    def delete_file(self, path, prefixed_path, source_storage): ...
    def link_file(self, path, prefixed_path, source_storage): ...
    def copy_file(self, path, prefixed_path, source_storage): ...
