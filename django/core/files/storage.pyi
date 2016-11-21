# Stubs for django.core.files.storage (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.utils.functional import LazyObject

class Storage:
    def open(self, name, mode: str = ...): ...
    def save(self, name, content, max_length: Optional[Any] = ...): ...
    def get_valid_name(self, name): ...
    def get_available_name(self, name, max_length: Optional[Any] = ...): ...
    def generate_filename(self, filename): ...
    def path(self, name): ...
    def delete(self, name): ...
    def exists(self, name): ...
    def listdir(self, path): ...
    def size(self, name): ...
    def url(self, name): ...
    def accessed_time(self, name): ...
    def created_time(self, name): ...
    def modified_time(self, name): ...
    def get_accessed_time(self, name): ...
    def get_created_time(self, name): ...
    def get_modified_time(self, name): ...

class FileSystemStorage(Storage):
    def __init__(self, location: Optional[Any] = ..., base_url: Optional[Any] = ..., file_permissions_mode: Optional[Any] = ..., directory_permissions_mode: Optional[Any] = ...) -> None: ...
    def base_location(self): ...
    def location(self): ...
    def base_url(self): ...
    def file_permissions_mode(self): ...
    def directory_permissions_mode(self): ...
    def delete(self, name): ...
    def exists(self, name): ...
    def listdir(self, path): ...
    def path(self, name): ...
    def size(self, name): ...
    def url(self, name): ...
    def accessed_time(self, name): ...
    def created_time(self, name): ...
    def modified_time(self, name): ...
    def get_accessed_time(self, name): ...
    def get_created_time(self, name): ...
    def get_modified_time(self, name): ...

class DefaultStorage(LazyObject): ...

default_storage = ...  # type: Any
