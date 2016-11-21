# Stubs for django.contrib.admin.views.main (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

ALL_VAR = ...  # type: str
ORDER_VAR = ...  # type: str
ORDER_TYPE_VAR = ...  # type: str
PAGE_VAR = ...  # type: str
SEARCH_VAR = ...  # type: str
ERROR_FLAG = ...  # type: str
IGNORED_PARAMS = ...  # type: Any

class ChangeList:
    model = ...  # type: Any
    opts = ...  # type: Any
    lookup_opts = ...  # type: Any
    root_queryset = ...  # type: Any
    list_display = ...  # type: Any
    list_display_links = ...  # type: Any
    list_filter = ...  # type: Any
    date_hierarchy = ...  # type: Any
    search_fields = ...  # type: Any
    list_select_related = ...  # type: Any
    list_per_page = ...  # type: Any
    list_max_show_all = ...  # type: Any
    model_admin = ...  # type: Any
    preserved_filters = ...  # type: Any
    page_num = ...  # type: Any
    show_all = ...  # type: Any
    is_popup = ...  # type: Any
    to_field = ...  # type: Any
    params = ...  # type: Any
    list_editable = ...  # type: Any
    query = ...  # type: Any
    queryset = ...  # type: Any
    title = ...  # type: Any
    pk_attname = ...  # type: Any
    def __init__(self, request, model, list_display, list_display_links, list_filter, date_hierarchy, search_fields, list_select_related, list_per_page, list_max_show_all, list_editable, model_admin) -> None: ...
    def get_filters_params(self, params: Optional[Any] = ...): ...
    def get_filters(self, request): ...
    def get_query_string(self, new_params: Optional[Any] = ..., remove: Optional[Any] = ...): ...
    result_count = ...  # type: Any
    show_full_result_count = ...  # type: Any
    show_admin_actions = ...  # type: Any
    full_result_count = ...  # type: Any
    result_list = ...  # type: Any
    can_show_all = ...  # type: Any
    multi_page = ...  # type: Any
    paginator = ...  # type: Any
    def get_results(self, request): ...
    def get_ordering_field(self, field_name): ...
    def get_ordering(self, request, queryset): ...
    def get_ordering_field_columns(self): ...
    def get_queryset(self, request): ...
    def apply_select_related(self, qs): ...
    def has_related_field_in_list_display(self): ...
    def url_for_result(self, result): ...
