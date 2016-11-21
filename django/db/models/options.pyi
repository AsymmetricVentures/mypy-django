# Stubs for django.db.models.options (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

NOT_PROVIDED = ...  # type: Any
PROXY_PARENTS = ...  # type: Any
EMPTY_RELATION_TREE = ...  # type: Any
IMMUTABLE_WARNING = ...  # type: str
DEFAULT_NAMES = ...  # type: Any

def normalize_together(option_together): ...
def make_immutable_fields_list(name, data): ...

class Options:
    FORWARD_PROPERTIES = ...  # type: Any
    REVERSE_PROPERTIES = ...  # type: Any
    default_apps = ...  # type: Any
    local_fields = ...  # type: Any
    local_many_to_many = ...  # type: Any
    private_fields = ...  # type: Any
    manager_inheritance_from_future = ...  # type: bool
    local_managers = ...  # type: Any
    base_manager_name = ...  # type: Any
    default_manager_name = ...  # type: Any
    model_name = ...  # type: Any
    verbose_name = ...  # type: Any
    verbose_name_plural = ...  # type: Any
    db_table = ...  # type: str
    ordering = ...  # type: Any
    unique_together = ...  # type: Any
    index_together = ...  # type: Any
    select_on_save = ...  # type: bool
    default_permissions = ...  # type: Any
    permissions = ...  # type: Any
    object_name = ...  # type: Any
    app_label = ...  # type: Any
    get_latest_by = ...  # type: Any
    order_with_respect_to = ...  # type: Any
    db_tablespace = ...  # type: Any
    required_db_features = ...  # type: Any
    required_db_vendor = ...  # type: Any
    meta = ...  # type: Any
    pk = ...  # type: Any
    has_auto_field = ...  # type: bool
    auto_field = ...  # type: Any
    abstract = ...  # type: bool
    managed = ...  # type: bool
    proxy = ...  # type: bool
    proxy_for_model = ...  # type: Any
    concrete_model = ...  # type: Any
    swappable = ...  # type: Any
    parents = ...  # type: Any
    auto_created = ...  # type: bool
    related_fkey_lookups = ...  # type: Any
    apps = ...  # type: Any
    default_related_name = ...  # type: Any
    def __init__(self, meta, app_label: Optional[Any] = ...) -> None: ...
    @property
    def label(self): ...
    @property
    def label_lower(self): ...
    @property
    def app_config(self): ...
    @property
    def installed(self): ...
    model = ...  # type: Any
    original_attrs = ...  # type: Any
    def contribute_to_class(self, cls, name): ...
    def add_manager(self, manager): ...
    def add_field(self, field, private: bool = ..., virtual: Any = ...): ...
    def setup_pk(self, field): ...
    def setup_proxy(self, target): ...
    def can_migrate(self, connection): ...
    @property
    def verbose_name_raw(self): ...
    @property
    def swapped(self): ...
    def managers(self): ...
    def managers_map(self): ...
    def base_manager(self): ...
    def default_manager(self): ...
    def fields(self): ...
    def concrete_fields(self): ...
    @property
    def virtual_fields(self): ...
    def local_concrete_fields(self): ...
    def many_to_many(self): ...
    def related_objects(self): ...
    def fields_map(self): ...
    def get_field(self, field_name): ...
    def get_base_chain(self, model): ...
    def get_parent_list(self): ...
    def get_ancestor_link(self, ancestor): ...
    def get_fields(self, include_parents: bool = ..., include_hidden: bool = ...): ...
