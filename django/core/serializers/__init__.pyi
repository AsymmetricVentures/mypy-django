# Stubs for django.core.serializers (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

BUILTIN_SERIALIZERS = ...  # type: Any

class BadSerializer:
    internal_use_only = ...  # type: bool
    exception = ...  # type: Any
    def __init__(self, exception) -> None: ...
    def __call__(self, *args, **kwargs): ...

def register_serializer(format, serializer_module, serializers: Optional[Any] = ...): ...
def unregister_serializer(format): ...
def get_serializer(format): ...
def get_serializer_formats(): ...
def get_public_serializer_formats(): ...
def get_deserializer(format): ...
def serialize(format, queryset, **options): ...
def deserialize(format, stream_or_string, **options): ...
def sort_dependencies(app_list): ...
