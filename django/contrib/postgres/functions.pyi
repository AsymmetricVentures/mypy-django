# Stubs for django.contrib.postgres.functions (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.db.models import Func

class TransactionNow(Func):
    template = ...  # type: str
    def __init__(self, output_field: Optional[Any] = ..., **extra) -> None: ...