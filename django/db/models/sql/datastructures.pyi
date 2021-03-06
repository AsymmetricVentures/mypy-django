# Stubs for django.db.models.sql.datastructures (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class EmptyResultSet(Exception): ...

class MultiJoin(Exception):
    level = ...  # type: Any
    names_with_path = ...  # type: Any
    def __init__(self, names_pos, path_with_names) -> None: ...

class Empty: ...

class Join:
    table_name = ...  # type: Any
    parent_alias = ...  # type: Any
    table_alias = ...  # type: Any
    join_type = ...  # type: Any
    join_cols = ...  # type: Any
    join_field = ...  # type: Any
    nullable = ...  # type: Any
    def __init__(self, table_name, parent_alias, table_alias, join_type, join_field, nullable) -> None: ...
    def as_sql(self, compiler, connection): ...
    def relabeled_clone(self, change_map): ...
    def __eq__(self, other): ...
    def demote(self): ...
    def promote(self): ...

class BaseTable:
    join_type = ...  # type: Any
    parent_alias = ...  # type: Any
    table_name = ...  # type: Any
    table_alias = ...  # type: Any
    def __init__(self, table_name, alias) -> None: ...
    def as_sql(self, compiler, connection): ...
    def relabeled_clone(self, change_map): ...
