# Stubs for django.forms.fields (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.utils.translation import ugettext_lazy as _

class Field:
    widget = ...  # type: Any
    hidden_widget = ...  # type: Any
    default_validators = ...  # type: Any
    default_error_messages = ...  # type: Any
    empty_values = ...  # type: Any
    creation_counter = ...  # type: int
    show_hidden_initial = ...  # type: Any
    help_text = ...  # type: Any
    disabled = ...  # type: Any
    label_suffix = ...  # type: Any
    localize = ...  # type: Any
    error_messages = ...  # type: Any
    validators = ...  # type: Any
    def __init__(self, required: bool = ..., widget: Optional[Any] = ..., label: Optional[Any] = ..., initial: Optional[Any] = ..., help_text: str = ..., error_messages: Optional[Any] = ..., show_hidden_initial: bool = ..., validators: Any = ..., localize: bool = ..., disabled: bool = ..., label_suffix: Optional[Any] = ...) -> None: ...
    def prepare_value(self, value): ...
    def to_python(self, value): ...
    def validate(self, value): ...
    def run_validators(self, value): ...
    def clean(self, value): ...
    def bound_data(self, data, initial): ...
    def widget_attrs(self, widget): ...
    def has_changed(self, initial, data): ...
    def get_bound_field(self, form, field_name): ...
    def __deepcopy__(self, memo): ...

class CharField(Field):
    max_length = ...  # type: Any
    min_length = ...  # type: Any
    strip = ...  # type: Any
    def __init__(self, max_length: Optional[Any] = ..., min_length: Optional[Any] = ..., strip: bool = ..., *args, **kwargs) -> None: ...
    def to_python(self, value): ...
    def widget_attrs(self, widget): ...

class IntegerField(Field):
    widget = ...  # type: Any
    default_error_messages = ...  # type: Any
    re_decimal = ...  # type: Any
    def __init__(self, max_value: Optional[Any] = ..., min_value: Optional[Any] = ..., *args, **kwargs) -> None: ...
    def to_python(self, value): ...
    def widget_attrs(self, widget): ...

class FloatField(IntegerField):
    default_error_messages = ...  # type: Any
    def to_python(self, value): ...
    def validate(self, value): ...
    def widget_attrs(self, widget): ...

class DecimalField(IntegerField):
    default_error_messages = ...  # type: Any
    def __init__(self, max_value: Optional[Any] = ..., min_value: Optional[Any] = ..., max_digits: Optional[Any] = ..., decimal_places: Optional[Any] = ..., *args, **kwargs) -> None: ...
    def to_python(self, value): ...
    def validate(self, value): ...
    def widget_attrs(self, widget): ...

class BaseTemporalField(Field):
    input_formats = ...  # type: Any
    def __init__(self, input_formats: Optional[Any] = ..., *args, **kwargs) -> None: ...
    def to_python(self, value): ...
    def strptime(self, value, format): ...

class DateField(BaseTemporalField):
    widget = ...  # type: Any
    input_formats = ...  # type: Any
    default_error_messages = ...  # type: Any
    def to_python(self, value): ...
    def strptime(self, value, format): ...

class TimeField(BaseTemporalField):
    widget = ...  # type: Any
    input_formats = ...  # type: Any
    default_error_messages = ...  # type: Any
    def to_python(self, value): ...
    def strptime(self, value, format): ...

class DateTimeField(BaseTemporalField):
    widget = ...  # type: Any
    input_formats = ...  # type: Any
    default_error_messages = ...  # type: Any
    def prepare_value(self, value): ...
    def to_python(self, value): ...
    def strptime(self, value, format): ...

class DurationField(Field):
    default_error_messages = ...  # type: Any
    def prepare_value(self, value): ...
    def to_python(self, value): ...

class RegexField(CharField):
    def __init__(self, regex, max_length: Optional[Any] = ..., min_length: Optional[Any] = ..., error_message: Optional[Any] = ..., *args, **kwargs) -> None: ...
    regex = ...  # type: Any

class EmailField(CharField):
    widget = ...  # type: Any
    default_validators = ...  # type: Any
    def clean(self, value): ...

class FileField(Field):
    widget = ...  # type: Any
    default_error_messages = ...  # type: Any
    max_length = ...  # type: Any
    allow_empty_file = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def to_python(self, data): ...
    def clean(self, data, initial: Optional[Any] = ...): ...
    def bound_data(self, data, initial): ...
    def has_changed(self, initial, data): ...

class ImageField(FileField):
    default_error_messages = ...  # type: Any
    def to_python(self, data): ...

class URLField(CharField):
    widget = ...  # type: Any
    default_error_messages = ...  # type: Any
    default_validators = ...  # type: Any
    def to_python(self, value): ...
    def clean(self, value): ...

class BooleanField(Field):
    widget = ...  # type: Any
    def to_python(self, value): ...
    def validate(self, value): ...
    def has_changed(self, initial, data): ...

class NullBooleanField(BooleanField):
    widget = ...  # type: Any
    def to_python(self, value): ...
    def validate(self, value): ...

class CallableChoiceIterator:
    choices_func = ...  # type: Any
    def __init__(self, choices_func) -> None: ...
    def __iter__(self): ...

class ChoiceField(Field):
    widget = ...  # type: Any
    default_error_messages = ...  # type: Any
    choices = ...  # type: Any
    def __init__(self, choices: Any = ..., required: bool = ..., widget: Optional[Any] = ..., label: Optional[Any] = ..., initial: Optional[Any] = ..., help_text: str = ..., *args, **kwargs) -> None: ...
    def __deepcopy__(self, memo): ...
    def to_python(self, value): ...
    def validate(self, value): ...
    def valid_value(self, value): ...

class TypedChoiceField(ChoiceField):
    coerce = ...  # type: Any
    empty_value = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def clean(self, value): ...

class MultipleChoiceField(ChoiceField):
    hidden_widget = ...  # type: Any
    widget = ...  # type: Any
    default_error_messages = ...  # type: Any
    def to_python(self, value): ...
    def validate(self, value): ...
    def has_changed(self, initial, data): ...

class TypedMultipleChoiceField(MultipleChoiceField):
    coerce = ...  # type: Any
    empty_value = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def clean(self, value): ...
    def validate(self, value): ...

class ComboField(Field):
    fields = ...  # type: Any
    def __init__(self, fields: Any = ..., *args, **kwargs) -> None: ...
    def clean(self, value): ...

class MultiValueField(Field):
    default_error_messages = ...  # type: Any
    require_all_fields = ...  # type: Any
    fields = ...  # type: Any
    def __init__(self, fields: Any = ..., *args, **kwargs) -> None: ...
    def __deepcopy__(self, memo): ...
    def validate(self, value): ...
    def clean(self, value): ...
    def compress(self, data_list): ...
    def has_changed(self, initial, data): ...

class FilePathField(ChoiceField):
    choices = ...  # type: Any
    match_re = ...  # type: Any
    def __init__(self, path, match: Optional[Any] = ..., recursive: bool = ..., allow_files: bool = ..., allow_folders: bool = ..., required: bool = ..., widget: Optional[Any] = ..., label: Optional[Any] = ..., initial: Optional[Any] = ..., help_text: str = ..., *args, **kwargs) -> None: ...

class SplitDateTimeField(MultiValueField):
    widget = ...  # type: Any
    hidden_widget = ...  # type: Any
    default_error_messages = ...  # type: Any
    def __init__(self, input_date_formats: Optional[Any] = ..., input_time_formats: Optional[Any] = ..., *args, **kwargs) -> None: ...
    def compress(self, data_list): ...

class GenericIPAddressField(CharField):
    unpack_ipv4 = ...  # type: Any
    default_validators = ...  # type: Any
    def __init__(self, protocol: str = ..., unpack_ipv4: bool = ..., *args, **kwargs) -> None: ...
    def to_python(self, value): ...

class SlugField(CharField):
    default_validators = ...  # type: Any
    allow_unicode = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...

class UUIDField(CharField):
    default_error_messages = ...  # type: Any
    def prepare_value(self, value): ...
    def to_python(self, value): ...