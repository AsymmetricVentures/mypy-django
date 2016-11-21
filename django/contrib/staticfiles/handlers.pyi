# Stubs for django.contrib.staticfiles.handlers (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.core.handlers.wsgi import WSGIHandler

class StaticFilesHandler(WSGIHandler):
    handles_files = ...  # type: bool
    application = ...  # type: Any
    base_url = ...  # type: Any
    def __init__(self, application) -> None: ...
    def get_base_url(self): ...
    def file_path(self, url): ...
    def serve(self, request): ...
    def get_response(self, request): ...
    def __call__(self, environ, start_response): ...