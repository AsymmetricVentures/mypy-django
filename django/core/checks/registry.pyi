# Stubs for django.core.checks.registry (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class Tags:
    admin = ...  # type: str
    caches = ...  # type: str
    compatibility = ...  # type: str
    database = ...  # type: str
    models = ...  # type: str
    security = ...  # type: str
    signals = ...  # type: str
    templates = ...  # type: str
    urls = ...  # type: str

class CheckRegistry:
    registered_checks = ...  # type: Any
    deployment_checks = ...  # type: Any
    def __init__(self) -> None: ...
    def register(self, check: Optional[Any] = ..., *tags, **kwargs): ...
    def run_checks(self, app_configs: Optional[Any] = ..., tags: Optional[Any] = ..., include_deployment_checks: bool = ...): ...
    def tag_exists(self, tag, include_deployment_checks: bool = ...): ...
    def tags_available(self, deployment_checks: bool = ...): ...
    def get_checks(self, include_deployment_checks: bool = ...): ...

registry = ...  # type: Any
register = ...  # type: Any
run_checks = ...  # type: Any
tag_exists = ...  # type: Any
