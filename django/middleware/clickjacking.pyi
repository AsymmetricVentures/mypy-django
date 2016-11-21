# Stubs for django.middleware.clickjacking (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.utils.deprecation import MiddlewareMixin

class XFrameOptionsMiddleware(MiddlewareMixin):
    def process_response(self, request, response): ...
    def get_xframe_options_value(self, request, response): ...