# Stubs for django.utils.baseconv (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

BASE2_ALPHABET = ...  # type: str
BASE16_ALPHABET = ...  # type: str
BASE56_ALPHABET = ...  # type: str
BASE36_ALPHABET = ...  # type: str
BASE62_ALPHABET = ...  # type: str
BASE64_ALPHABET = ...  # type: Any

class BaseConverter:
    decimal_digits = ...  # type: str
    sign = ...  # type: Any
    digits = ...  # type: Any
    def __init__(self, digits, sign: str = ...) -> None: ...
    def encode(self, i): ...
    def decode(self, s): ...
    def convert(self, number, from_digits, to_digits, sign): ...

base2 = ...  # type: Any
base16 = ...  # type: Any
base36 = ...  # type: Any
base56 = ...  # type: Any
base62 = ...  # type: Any
base64 = ...  # type: Any