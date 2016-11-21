# Stubs for django.db.backends.sqlite3.operations (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.db.backends import utils as backend_utils
from django.db.backends.base.operations import BaseDatabaseOperations

pytz = ...  # type: Any

class DatabaseOperations(BaseDatabaseOperations):
    def bulk_batch_size(self, fields, objs): ...
    def check_expression_support(self, expression): ...
    def date_extract_sql(self, lookup_type, field_name): ...
    def date_interval_sql(self, timedelta): ...
    def format_for_duration_arithmetic(self, sql): ...
    def date_trunc_sql(self, lookup_type, field_name): ...
    def datetime_cast_date_sql(self, field_name, tzname): ...
    def datetime_extract_sql(self, lookup_type, field_name, tzname): ...
    def datetime_trunc_sql(self, lookup_type, field_name, tzname): ...
    def time_extract_sql(self, lookup_type, field_name): ...
    def drop_foreignkey_sql(self): ...
    def pk_default_value(self): ...
    def last_executed_query(self, cursor, sql, params): ...
    def quote_name(self, name): ...
    def no_limit_value(self): ...
    def sql_flush(self, style, tables, sequences, allow_cascade: bool = ...): ...
    def adapt_datetimefield_value(self, value): ...
    def adapt_timefield_value(self, value): ...
    def get_db_converters(self, expression): ...
    def convert_datetimefield_value(self, value, expression, connection, context): ...
    def convert_datefield_value(self, value, expression, connection, context): ...
    def convert_timefield_value(self, value, expression, connection, context): ...
    def convert_decimalfield_value(self, value, expression, connection, context): ...
    def convert_uuidfield_value(self, value, expression, connection, context): ...
    def bulk_insert_sql(self, fields, placeholder_rows): ...
    def combine_expression(self, connector, sub_expressions): ...
    def combine_duration_expression(self, connector, sub_expressions): ...
    def integer_field_range(self, internal_type): ...
    def subtract_temporals(self, internal_type, lhs, rhs): ...