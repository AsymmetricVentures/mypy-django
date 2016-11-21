# Stubs for django.db.backends.base.operations (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class BaseDatabaseOperations:
    compiler_module = ...  # type: str
    integer_field_ranges = ...  # type: Any
    connection = ...  # type: Any
    def __init__(self, connection) -> None: ...
    def autoinc_sql(self, table, column): ...
    def bulk_batch_size(self, fields, objs): ...
    def cache_key_culling_sql(self): ...
    def unification_cast_sql(self, output_field): ...
    def date_extract_sql(self, lookup_type, field_name): ...
    def date_interval_sql(self, timedelta): ...
    def date_trunc_sql(self, lookup_type, field_name): ...
    def datetime_cast_date_sql(self, field_name, tzname): ...
    def datetime_extract_sql(self, lookup_type, field_name, tzname): ...
    def datetime_trunc_sql(self, lookup_type, field_name, tzname): ...
    def time_extract_sql(self, lookup_type, field_name): ...
    def deferrable_sql(self): ...
    def distinct_sql(self, fields): ...
    def drop_foreignkey_sql(self): ...
    def drop_sequence_sql(self, table): ...
    def fetch_returned_insert_id(self, cursor): ...
    def field_cast_sql(self, db_type, internal_type): ...
    def force_no_ordering(self): ...
    def for_update_sql(self, nowait: bool = ...): ...
    def fulltext_search_sql(self, field_name): ...
    def last_executed_query(self, cursor, sql, params): ...
    def last_insert_id(self, cursor, table_name, pk_name): ...
    def lookup_cast(self, lookup_type, internal_type: Optional[Any] = ...): ...
    def max_in_list_size(self): ...
    def max_name_length(self): ...
    def no_limit_value(self): ...
    def pk_default_value(self): ...
    def prepare_sql_script(self, sql): ...
    def process_clob(self, value): ...
    def return_insert_id(self): ...
    def compiler(self, compiler_name): ...
    def quote_name(self, name): ...
    def random_function_sql(self): ...
    def regex_lookup(self, lookup_type): ...
    def savepoint_create_sql(self, sid): ...
    def savepoint_commit_sql(self, sid): ...
    def savepoint_rollback_sql(self, sid): ...
    def set_time_zone_sql(self): ...
    def sql_flush(self, style, tables, sequences, allow_cascade: bool = ...): ...
    def sequence_reset_by_name_sql(self, style, sequences): ...
    def sequence_reset_sql(self, style, model_list): ...
    def start_transaction_sql(self): ...
    def end_transaction_sql(self, success: bool = ...): ...
    def tablespace_sql(self, tablespace, inline: bool = ...): ...
    def prep_for_like_query(self, x): ...
    prep_for_iexact_query = ...  # type: Any
    def validate_autopk_value(self, value): ...
    def adapt_unknown_value(self, value): ...
    def adapt_datefield_value(self, value): ...
    def adapt_datetimefield_value(self, value): ...
    def adapt_timefield_value(self, value): ...
    def adapt_decimalfield_value(self, value, max_digits: Optional[Any] = ..., decimal_places: Optional[Any] = ...): ...
    def adapt_ipaddressfield_value(self, value): ...
    def year_lookup_bounds_for_date_field(self, value): ...
    def year_lookup_bounds_for_datetime_field(self, value): ...
    def get_db_converters(self, expression): ...
    def convert_durationfield_value(self, value, expression, connection, context): ...
    def check_aggregate_support(self, aggregate_func): ...
    def check_expression_support(self, expression): ...
    def combine_expression(self, connector, sub_expressions): ...
    def combine_duration_expression(self, connector, sub_expressions): ...
    def binary_placeholder_sql(self, value): ...
    def modify_insert_params(self, placeholder, params): ...
    def integer_field_range(self, internal_type): ...
    def subtract_temporals(self, internal_type, lhs, rhs): ...
