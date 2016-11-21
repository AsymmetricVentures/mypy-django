# Stubs for django.middleware.common (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.utils.deprecation import MiddlewareMixin

logger = ...  # type: Any

class CommonMiddleware(MiddlewareMixin):
    response_redirect_class = ...  # type: Any
    def process_request(self, request): ...
    def should_redirect_with_slash(self, request): ...
    def get_full_path_with_slash(self, request): ...
    def process_response(self, request, response): ...

class BrokenLinkEmailsMiddleware(MiddlewareMixin):
    def process_response(self, request, response): ...
    def is_internal_request(self, domain, referer): ...
    def is_ignorable_request(self, request, uri, domain, referer): ...