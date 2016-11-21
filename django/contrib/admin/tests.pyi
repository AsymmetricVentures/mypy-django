# Stubs for django.contrib.admin.tests (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test.selenium import SeleniumTestCase
from django.utils.deprecation import MiddlewareMixin
from django.utils.translation import ugettext as _

class CSPMiddleware(MiddlewareMixin):
    def process_response(self, request, response): ...

class AdminSeleniumTestCase(SeleniumTestCase, StaticLiveServerTestCase):
    available_apps = ...  # type: Any
    def wait_until(self, callback, timeout: int = ...): ...
    def wait_for_popup(self, num_windows: int = ..., timeout: int = ...): ...
    def wait_for(self, css_selector, timeout: int = ...): ...
    def wait_for_text(self, css_selector, text, timeout: int = ...): ...
    def wait_for_value(self, css_selector, text, timeout: int = ...): ...
    def wait_until_visible(self, css_selector, timeout: int = ...): ...
    def wait_until_invisible(self, css_selector, timeout: int = ...): ...
    def wait_page_loaded(self): ...
    def admin_login(self, username, password, login_url: str = ...): ...
    def get_css_value(self, selector, attribute): ...
    def get_select_option(self, selector, value): ...
    def assertSelectOptions(self, selector, values): ...
    def assertSelectedOptions(self, selector, values): ...
    def has_css_class(self, selector, klass): ...