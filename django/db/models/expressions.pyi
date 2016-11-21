# Stubs for django.db.models.expressions (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.db.backends import utils as backend_utils

class Combinable:
    ADD = ...  # type: str
    SUB = ...  # type: str
    MUL = ...  # type: str
    DIV = ...  # type: str
    POW = ...  # type: str
    MOD = ...  # type: str
    BITAND = ...  # type: str
    BITOR = ...  # type: str
    def __add__(self, other): ...
    def __sub__(self, other): ...
    def __mul__(self, other): ...
    def __truediv__(self, other): ...
    def __div__(self, other): ...
    def __mod__(self, other): ...
    def __pow__(self, other): ...
    def __and__(self, other): ...
    def bitand(self, other): ...
    def __or__(self, other): ...
    def bitor(self, other): ...
    def __radd__(self, other): ...
    def __rsub__(self, other): ...
    def __rmul__(self, other): ...
    def __rtruediv__(self, other): ...
    def __rdiv__(self, other): ...
    def __rmod__(self, other): ...
    def __rpow__(self, other): ...
    def __rand__(self, other): ...
    def __ror__(self, other): ...

class BaseExpression:
    is_summary = ...  # type: bool
    def __init__(self, output_field: Optional[Any] = ...) -> None: ...
    def get_db_converters(self, connection): ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs): ...
    def as_sql(self, compiler, connection): ...
    def contains_aggregate(self): ...
    def contains_column_references(self): ...
    def resolve_expression(self, query: Optional[Any] = ..., allow_joins: bool = ..., reuse: Optional[Any] = ..., summarize: bool = ..., for_save: bool = ...): ...
    @property
    def field(self): ...
    def output_field(self): ...
    def convert_value(self, value, expression, connection, context): ...
    def get_lookup(self, lookup): ...
    def get_transform(self, name): ...
    def relabeled_clone(self, change_map): ...
    def copy(self): ...
    def get_group_by_cols(self): ...
    def get_source_fields(self): ...
    def asc(self): ...
    def desc(self): ...
    def reverse_ordering(self): ...
    def flatten(self): ...

class Expression(BaseExpression, Combinable): ...

class CombinedExpression(Expression):
    connector = ...  # type: Any
    lhs = ...  # type: Any
    rhs = ...  # type: Any
    def __init__(self, lhs, connector, rhs, output_field: Optional[Any] = ...) -> None: ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs): ...
    def as_sql(self, compiler, connection): ...
    def resolve_expression(self, query: Optional[Any] = ..., allow_joins: bool = ..., reuse: Optional[Any] = ..., summarize: bool = ..., for_save: bool = ...): ...

class DurationExpression(CombinedExpression):
    def compile(self, side, compiler, connection): ...
    def as_sql(self, compiler, connection): ...

class TemporalSubtraction(CombinedExpression):
    def __init__(self, lhs, rhs) -> None: ...
    def as_sql(self, compiler, connection): ...

class F(Combinable):
    name = ...  # type: Any
    def __init__(self, name) -> None: ...
    def resolve_expression(self, query: Optional[Any] = ..., allow_joins: bool = ..., reuse: Optional[Any] = ..., summarize: bool = ..., for_save: bool = ...): ...
    def asc(self): ...
    def desc(self): ...

class Func(Expression):
    function = ...  # type: Any
    template = ...  # type: str
    arg_joiner = ...  # type: str
    arity = ...  # type: Any
    source_expressions = ...  # type: Any
    extra = ...  # type: Any
    def __init__(self, *expressions, **extra) -> None: ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs): ...
    def resolve_expression(self, query: Optional[Any] = ..., allow_joins: bool = ..., reuse: Optional[Any] = ..., summarize: bool = ..., for_save: bool = ...): ...
    def as_sql(self, compiler, connection, function: Optional[Any] = ..., template: Optional[Any] = ..., arg_joiner: Optional[Any] = ..., **extra_context): ...
    def as_sqlite(self, compiler, connection): ...
    def copy(self): ...

class Value(Expression):
    value = ...  # type: Any
    def __init__(self, value, output_field: Optional[Any] = ...) -> None: ...
    def as_sql(self, compiler, connection): ...
    def resolve_expression(self, query: Optional[Any] = ..., allow_joins: bool = ..., reuse: Optional[Any] = ..., summarize: bool = ..., for_save: bool = ...): ...
    def get_group_by_cols(self): ...

class DurationValue(Value):
    def as_sql(self, compiler, connection): ...

class RawSQL(Expression):
    def __init__(self, sql, params, output_field: Optional[Any] = ...) -> None: ...
    def as_sql(self, compiler, connection): ...
    def get_group_by_cols(self): ...

class Star(Expression):
    def as_sql(self, compiler, connection): ...

class Random(Expression):
    def __init__(self) -> None: ...
    def as_sql(self, compiler, connection): ...

class Col(Expression):
    contains_column_references = ...  # type: bool
    def __init__(self, alias, target, output_field: Optional[Any] = ...) -> None: ...
    def as_sql(self, compiler, connection): ...
    def relabeled_clone(self, relabels): ...
    def get_group_by_cols(self): ...
    def get_db_converters(self, connection): ...

class Ref(Expression):
    def __init__(self, refs, source) -> None: ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs): ...
    def resolve_expression(self, query: Optional[Any] = ..., allow_joins: bool = ..., reuse: Optional[Any] = ..., summarize: bool = ..., for_save: bool = ...): ...
    def relabeled_clone(self, relabels): ...
    def as_sql(self, compiler, connection): ...
    def get_group_by_cols(self): ...

class ExpressionWrapper(Expression):
    expression = ...  # type: Any
    def __init__(self, expression, output_field) -> None: ...
    def set_source_expressions(self, exprs): ...
    def get_source_expressions(self): ...
    def as_sql(self, compiler, connection): ...

class When(Expression):
    template = ...  # type: str
    condition = ...  # type: Any
    result = ...  # type: Any
    def __init__(self, condition: Optional[Any] = ..., then: Optional[Any] = ..., **lookups) -> None: ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs): ...
    def get_source_fields(self): ...
    def resolve_expression(self, query: Optional[Any] = ..., allow_joins: bool = ..., reuse: Optional[Any] = ..., summarize: bool = ..., for_save: bool = ...): ...
    def as_sql(self, compiler, connection, template: Optional[Any] = ..., **extra_context): ...
    def get_group_by_cols(self): ...

class Case(Expression):
    template = ...  # type: str
    case_joiner = ...  # type: str
    cases = ...  # type: Any
    default = ...  # type: Any
    extra = ...  # type: Any
    def __init__(self, *cases, **extra) -> None: ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs): ...
    def resolve_expression(self, query: Optional[Any] = ..., allow_joins: bool = ..., reuse: Optional[Any] = ..., summarize: bool = ..., for_save: bool = ...): ...
    def copy(self): ...
    def as_sql(self, compiler, connection, template: Optional[Any] = ..., case_joiner: Optional[Any] = ..., **extra_context): ...

class OrderBy(BaseExpression):
    template = ...  # type: str
    descending = ...  # type: Any
    expression = ...  # type: Any
    def __init__(self, expression, descending: bool = ...) -> None: ...
    def set_source_expressions(self, exprs): ...
    def get_source_expressions(self): ...
    def as_sql(self, compiler, connection, template: Optional[Any] = ..., **extra_context): ...
    def get_group_by_cols(self): ...
    def reverse_ordering(self): ...
    def asc(self): ...
    def desc(self): ...