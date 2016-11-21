# Stubs for django.db (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.db.utils import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, DJANGO_VERSION_PICKLE_KEY as DJANGO_VERSION_PICKLE_KEY, DatabaseError as DatabaseError, DataError as DataError, Error as Error, IntegrityError as IntegrityError, InterfaceError as InterfaceError, InternalError as InternalError, NotSupportedError as NotSupportedError, OperationalError as OperationalError, ProgrammingError as ProgrammingError

connections = ...  # type: Any
router = ...  # type: Any

class DefaultConnectionProxy:
    def __getattr__(self, item): ...
    def __setattr__(self, name, value): ...
    def __delattr__(self, name): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

connection = ...  # type: Any
