# Stubs for django.middleware.gzip (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.utils.deprecation import MiddlewareMixin

re_accepts_gzip = ...  # type: Any

class GZipMiddleware(MiddlewareMixin):
    def process_response(self, request, response): ...
