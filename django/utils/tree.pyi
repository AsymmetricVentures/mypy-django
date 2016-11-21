# Stubs for django.utils.tree (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class Node:
    default = ...  # type: str
    children = ...  # type: Any
    connector = ...  # type: Any
    negated = ...  # type: Any
    def __init__(self, children: Optional[Any] = ..., connector: Optional[Any] = ..., negated: bool = ...) -> None: ...
    def __deepcopy__(self, memodict): ...
    def __len__(self): ...
    def __bool__(self): ...
    def __nonzero__(self): ...
    def __contains__(self, other): ...
    def add(self, data, conn_type, squash: bool = ...): ...
    def negate(self): ...