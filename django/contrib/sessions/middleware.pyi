# Stubs for django.contrib.sessions.middleware (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.utils.deprecation import MiddlewareMixin

class SessionMiddleware(MiddlewareMixin):
    get_response = ...  # type: Any
    SessionStore = ...  # type: Any
    def __init__(self, get_response: Optional[Any] = ...) -> None: ...
    def process_request(self, request): ...
    def process_response(self, request, response): ...
