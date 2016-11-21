# Stubs for django.utils.safestring (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import six

class EscapeData: ...
class EscapeBytes(bytes, EscapeData): ...
class EscapeText(six.text_type, EscapeData): ...

EscapeString = ...  # type: Any
EscapeUnicode = ...  # type: Any

class SafeData:
    def __html__(self): ...

class SafeBytes(bytes, SafeData):
    def __add__(self, rhs): ...
    decode = ...  # type: Any

class SafeText(six.text_type, SafeData):
    def __add__(self, rhs): ...
    encode = ...  # type: Any

SafeString = ...  # type: Any
SafeUnicode = ...  # type: Any

def mark_safe(s): ...
def mark_for_escaping(s): ...
