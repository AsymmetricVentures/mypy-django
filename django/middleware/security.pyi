# Stubs for django.middleware.security (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.utils.deprecation import MiddlewareMixin

class SecurityMiddleware(MiddlewareMixin):
    sts_seconds = ...  # type: Any
    sts_include_subdomains = ...  # type: Any
    content_type_nosniff = ...  # type: Any
    xss_filter = ...  # type: Any
    redirect = ...  # type: Any
    redirect_host = ...  # type: Any
    redirect_exempt = ...  # type: Any
    get_response = ...  # type: Any
    def __init__(self, get_response: Optional[Any] = ...) -> None: ...
    def process_request(self, request): ...
    def process_response(self, request, response): ...