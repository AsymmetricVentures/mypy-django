# Stubs for django.db.migrations.operations.models (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.db.migrations.operations.base import Operation
from .fields import AddField as AddField, AlterField as AlterField, FieldOperation as FieldOperation, RemoveField as RemoveField, RenameField as RenameField

class ModelOperation(Operation):
    name = ...  # type: Any
    def __init__(self, name) -> None: ...
    def name_lower(self): ...
    def references_model(self, name, app_label: Optional[Any] = ...): ...
    def reduce(self, operation, in_between, app_label: Optional[Any] = ...): ...

class CreateModel(ModelOperation):
    serialization_expand_args = ...  # type: Any
    fields = ...  # type: Any
    options = ...  # type: Any
    bases = ...  # type: Any
    managers = ...  # type: Any
    def __init__(self, name, fields, options: Optional[Any] = ..., bases: Optional[Any] = ..., managers: Optional[Any] = ...) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label, state): ...
    def database_forwards(self, app_label, schema_editor, from_state, to_state): ...
    def database_backwards(self, app_label, schema_editor, from_state, to_state): ...
    def describe(self): ...
    def references_model(self, name, app_label: Optional[Any] = ...): ...
    def model_to_key(self, model): ...
    def reduce(self, operation, in_between, app_label: Optional[Any] = ...): ...

class DeleteModel(ModelOperation):
    def deconstruct(self): ...
    def state_forwards(self, app_label, state): ...
    def database_forwards(self, app_label, schema_editor, from_state, to_state): ...
    def database_backwards(self, app_label, schema_editor, from_state, to_state): ...
    def describe(self): ...

class RenameModel(ModelOperation):
    old_name = ...  # type: Any
    new_name = ...  # type: Any
    def __init__(self, old_name, new_name) -> None: ...
    def old_name_lower(self): ...
    def new_name_lower(self): ...
    def deconstruct(self): ...
    def state_forwards(self, app_label, state): ...
    def database_forwards(self, app_label, schema_editor, from_state, to_state): ...
    def database_backwards(self, app_label, schema_editor, from_state, to_state): ...
    def references_model(self, name, app_label: Optional[Any] = ...): ...
    def describe(self): ...
    def reduce(self, operation, in_between, app_label: Optional[Any] = ...): ...

class AlterModelTable(ModelOperation):
    table = ...  # type: Any
    def __init__(self, name, table) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label, state): ...
    def database_forwards(self, app_label, schema_editor, from_state, to_state): ...
    def database_backwards(self, app_label, schema_editor, from_state, to_state): ...
    def describe(self): ...
    def reduce(self, operation, in_between, app_label: Optional[Any] = ...): ...

class ModelOptionOperation(ModelOperation):
    def reduce(self, operation, in_between, app_label: Optional[Any] = ...): ...

class FieldRelatedOptionOperation(ModelOptionOperation):
    def reduce(self, operation, in_between, app_label: Optional[Any] = ...): ...

class AlterUniqueTogether(FieldRelatedOptionOperation):
    option_name = ...  # type: str
    unique_together = ...  # type: Any
    def __init__(self, name, unique_together) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label, state): ...
    def database_forwards(self, app_label, schema_editor, from_state, to_state): ...
    def database_backwards(self, app_label, schema_editor, from_state, to_state): ...
    def references_field(self, model_name, name, app_label: Optional[Any] = ...): ...
    def describe(self): ...

class AlterIndexTogether(FieldRelatedOptionOperation):
    option_name = ...  # type: str
    index_together = ...  # type: Any
    def __init__(self, name, index_together) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label, state): ...
    def database_forwards(self, app_label, schema_editor, from_state, to_state): ...
    def database_backwards(self, app_label, schema_editor, from_state, to_state): ...
    def references_field(self, model_name, name, app_label: Optional[Any] = ...): ...
    def describe(self): ...

class AlterOrderWithRespectTo(FieldRelatedOptionOperation):
    order_with_respect_to = ...  # type: Any
    def __init__(self, name, order_with_respect_to) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label, state): ...
    def database_forwards(self, app_label, schema_editor, from_state, to_state): ...
    def database_backwards(self, app_label, schema_editor, from_state, to_state): ...
    def references_field(self, model_name, name, app_label: Optional[Any] = ...): ...
    def describe(self): ...

class AlterModelOptions(ModelOptionOperation):
    ALTER_OPTION_KEYS = ...  # type: Any
    options = ...  # type: Any
    def __init__(self, name, options) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label, state): ...
    def database_forwards(self, app_label, schema_editor, from_state, to_state): ...
    def database_backwards(self, app_label, schema_editor, from_state, to_state): ...
    def describe(self): ...

class AlterModelManagers(ModelOptionOperation):
    serialization_expand_args = ...  # type: Any
    managers = ...  # type: Any
    def __init__(self, name, managers) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label, state): ...
    def database_forwards(self, app_label, schema_editor, from_state, to_state): ...
    def database_backwards(self, app_label, schema_editor, from_state, to_state): ...
    def describe(self): ...