# Stubs for django.core.mail.backends.dummy (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.mail.backends.base import BaseEmailBackend

class EmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages): ...
