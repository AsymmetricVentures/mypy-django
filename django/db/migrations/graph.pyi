# Stubs for django.db.migrations.graph (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .exceptions import CircularDependencyError as CircularDependencyError, NodeNotFoundError as NodeNotFoundError

RECURSION_DEPTH_WARNING = ...  # type: str

class Node:
    key = ...  # type: Any
    children = ...  # type: Any
    parents = ...  # type: Any
    def __init__(self, key) -> None: ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self): ...
    def __getitem__(self, item): ...
    def add_child(self, child): ...
    def add_parent(self, parent): ...
    def ancestors(self): ...
    def descendants(self): ...

class DummyNode(Node):
    origin = ...  # type: Any
    error_message = ...  # type: Any
    def __init__(self, key, origin, error_message) -> None: ...
    __class__ = ...  # type: Any
    def promote(self): ...
    def raise_error(self): ...

class MigrationGraph:
    node_map = ...  # type: Any
    nodes = ...  # type: Any
    cached = ...  # type: bool
    def __init__(self) -> None: ...
    def add_node(self, key, migration): ...
    def add_dummy_node(self, key, origin, error_message): ...
    def add_dependency(self, migration, child, parent, skip_validation: bool = ...): ...
    def remove_replaced_nodes(self, replacement, replaced): ...
    def remove_replacement_node(self, replacement, replaced): ...
    def validate_consistency(self): ...
    def clear_cache(self): ...
    def forwards_plan(self, target): ...
    def backwards_plan(self, target): ...
    def iterative_dfs(self, start, forwards: bool = ...): ...
    def root_nodes(self, app: Optional[Any] = ...): ...
    def leaf_nodes(self, app: Optional[Any] = ...): ...
    def ensure_not_cyclic(self, start, get_children): ...
    def make_state(self, nodes: Optional[Any] = ..., at_end: bool = ..., real_apps: Optional[Any] = ...): ...
    def __contains__(self, node): ...