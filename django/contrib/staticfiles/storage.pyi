# Stubs for django.contrib.staticfiles.storage (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.core.cache import cache as default_cache
from django.core.files.storage import FileSystemStorage
from django.utils.functional import LazyObject

class StaticFilesStorage(FileSystemStorage):
    base_location = ...  # type: Any
    location = ...  # type: Any
    def __init__(self, location: Optional[Any] = ..., base_url: Optional[Any] = ..., *args, **kwargs) -> None: ...
    def path(self, name): ...

class HashedFilesMixin:
    default_template = ...  # type: str
    patterns = ...  # type: Any
    hashed_files = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def file_hash(self, name, content: Optional[Any] = ...): ...
    def hashed_name(self, name, content: Optional[Any] = ...): ...
    def url(self, name, force: bool = ...): ...
    def url_converter(self, name, template: Optional[Any] = ...): ...
    def post_process(self, paths, dry_run: bool = ..., **options): ...
    def clean_name(self, name): ...
    def hash_key(self, name): ...
    def stored_name(self, name): ...

class ManifestFilesMixin(HashedFilesMixin):
    manifest_version = ...  # type: str
    manifest_name = ...  # type: str
    hashed_files = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def read_manifest(self): ...
    def load_manifest(self): ...
    def post_process(self, *args, **kwargs): ...
    def save_manifest(self): ...

class _MappingCache:
    cache = ...  # type: Any
    def __init__(self, cache) -> None: ...
    def __setitem__(self, key, value): ...
    def __getitem__(self, key): ...
    def clear(self): ...
    def update(self, data): ...
    def get(self, key, default: Optional[Any] = ...): ...

class CachedFilesMixin(HashedFilesMixin):
    hashed_files = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def hash_key(self, name): ...

class CachedStaticFilesStorage(CachedFilesMixin, StaticFilesStorage): ...
class ManifestStaticFilesStorage(ManifestFilesMixin, StaticFilesStorage): ...
class ConfiguredStorage(LazyObject): ...

staticfiles_storage = ...  # type: Any