# Stubs for django.db.models.functions.datetime (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.db.models import Transform

class TimezoneMixin:
    tzinfo = ...  # type: Any
    def get_tzname(self): ...

class Extract(TimezoneMixin, Transform):
    lookup_name = ...  # type: Any
    tzinfo = ...  # type: Any
    def __init__(self, expression, lookup_name: Optional[Any] = ..., tzinfo: Optional[Any] = ..., **extra) -> None: ...
    def as_sql(self, compiler, connection): ...
    def resolve_expression(self, query: Optional[Any] = ..., allow_joins: bool = ..., reuse: Optional[Any] = ..., summarize: bool = ..., for_save: bool = ...): ...
    def output_field(self): ...

class ExtractYear(Extract):
    lookup_name = ...  # type: str

class ExtractMonth(Extract):
    lookup_name = ...  # type: str

class ExtractDay(Extract):
    lookup_name = ...  # type: str

class ExtractWeekDay(Extract):
    lookup_name = ...  # type: str

class ExtractHour(Extract):
    lookup_name = ...  # type: str

class ExtractMinute(Extract):
    lookup_name = ...  # type: str

class ExtractSecond(Extract):
    lookup_name = ...  # type: str

class TruncBase(TimezoneMixin, Transform):
    arity = ...  # type: int
    kind = ...  # type: Any
    tzinfo = ...  # type: Any
    def __init__(self, expression, output_field: Optional[Any] = ..., tzinfo: Optional[Any] = ..., **extra) -> None: ...
    def as_sql(self, compiler, connection): ...
    def resolve_expression(self, query: Optional[Any] = ..., allow_joins: bool = ..., reuse: Optional[Any] = ..., summarize: bool = ..., for_save: bool = ...): ...
    def convert_value(self, value, expression, connection, context): ...

class Trunc(TruncBase):
    kind = ...  # type: Any
    def __init__(self, expression, kind, output_field: Optional[Any] = ..., tzinfo: Optional[Any] = ..., **extra) -> None: ...

class TruncYear(TruncBase):
    kind = ...  # type: str

class TruncMonth(TruncBase):
    kind = ...  # type: str

class TruncDay(TruncBase):
    kind = ...  # type: str

class TruncDate(TruncBase):
    lookup_name = ...  # type: str
    def output_field(self): ...
    def as_sql(self, compiler, connection): ...

class TruncHour(TruncBase):
    kind = ...  # type: str
    def output_field(self): ...

class TruncMinute(TruncBase):
    kind = ...  # type: str
    def output_field(self): ...

class TruncSecond(TruncBase):
    kind = ...  # type: str
    def output_field(self): ...