# Stubs for django.contrib.sessions.backends.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

VALID_KEY_CHARS = ...  # type: Any

class CreateError(Exception): ...
class UpdateError(Exception): ...

class SessionBase:
    TEST_COOKIE_NAME = ...  # type: str
    TEST_COOKIE_VALUE = ...  # type: str
    accessed = ...  # type: bool
    modified = ...  # type: bool
    serializer = ...  # type: Any
    def __init__(self, session_key: Optional[Any] = ...) -> None: ...
    def __contains__(self, key): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...
    def get(self, key, default: Optional[Any] = ...): ...
    def pop(self, key, default: Any = ...): ...
    def setdefault(self, key, value): ...
    def set_test_cookie(self): ...
    def test_cookie_worked(self): ...
    def delete_test_cookie(self): ...
    def encode(self, session_dict): ...
    def decode(self, session_data): ...
    def update(self, dict_): ...
    def has_key(self, key): ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def iterkeys(self): ...
    def itervalues(self): ...
    def iteritems(self): ...
    def clear(self): ...
    def is_empty(self): ...
    session_key = ...  # type: Any
    def get_expiry_age(self, **kwargs): ...
    def get_expiry_date(self, **kwargs): ...
    def set_expiry(self, value): ...
    def get_expire_at_browser_close(self): ...
    def flush(self): ...
    def cycle_key(self): ...
    def exists(self, session_key): ...
    def create(self): ...
    def save(self, must_create: bool = ...): ...
    def delete(self, session_key: Optional[Any] = ...): ...
    def load(self): ...
    @classmethod
    def clear_expired(cls): ...
