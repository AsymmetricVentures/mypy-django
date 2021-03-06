# Stubs for django.forms.models (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.forms.fields import ChoiceField, Field
from django.forms.forms import BaseForm, DeclarativeFieldsMetaclass
from django.forms.formsets import BaseFormSet
from django.utils.translation import ugettext_lazy as _

ALL_FIELDS = ...  # type: str

def model_to_dict(instance, fields: Optional[Any] = ..., exclude: Optional[Any] = ...): ...
def fields_for_model(model, fields: Optional[Any] = ..., exclude: Optional[Any] = ..., widgets: Optional[Any] = ..., formfield_callback: Optional[Any] = ..., localized_fields: Optional[Any] = ..., labels: Optional[Any] = ..., help_texts: Optional[Any] = ..., error_messages: Optional[Any] = ..., field_classes: Optional[Any] = ...): ...

class ModelFormOptions:
    model = ...  # type: Any
    fields = ...  # type: Any
    exclude = ...  # type: Any
    widgets = ...  # type: Any
    localized_fields = ...  # type: Any
    labels = ...  # type: Any
    help_texts = ...  # type: Any
    error_messages = ...  # type: Any
    field_classes = ...  # type: Any
    def __init__(self, options: Optional[Any] = ...) -> None: ...

class ModelFormMetaclass(DeclarativeFieldsMetaclass):
    def __new__(mcs, name, bases, attrs): ...

class BaseModelForm(BaseForm):
    instance = ...  # type: Any
    def __init__(self, data: Optional[Any] = ..., files: Optional[Any] = ..., auto_id: str = ..., prefix: Optional[Any] = ..., initial: Optional[Any] = ..., error_class: Any = ..., label_suffix: Optional[Any] = ..., empty_permitted: bool = ..., instance: Optional[Any] = ..., use_required_attribute: Optional[Any] = ...) -> None: ...
    def clean(self): ...
    def validate_unique(self): ...
    save_m2m = ...  # type: Any
    def save(self, commit: bool = ...): ...

class ModelForm: ...

def modelform_factory(model, form: Any = ..., fields: Optional[Any] = ..., exclude: Optional[Any] = ..., formfield_callback: Optional[Any] = ..., widgets: Optional[Any] = ..., localized_fields: Optional[Any] = ..., labels: Optional[Any] = ..., help_texts: Optional[Any] = ..., error_messages: Optional[Any] = ..., field_classes: Optional[Any] = ...): ...

class BaseModelFormSet(BaseFormSet):
    model = ...  # type: Any
    unique_fields = ...  # type: Any
    queryset = ...  # type: Any
    initial_extra = ...  # type: Any
    def __init__(self, data: Optional[Any] = ..., files: Optional[Any] = ..., auto_id: str = ..., prefix: Optional[Any] = ..., queryset: Optional[Any] = ..., **kwargs) -> None: ...
    def initial_form_count(self): ...
    def get_queryset(self): ...
    def save_new(self, form, commit: bool = ...): ...
    def save_existing(self, form, instance, commit: bool = ...): ...
    def delete_existing(self, obj, commit: bool = ...): ...
    saved_forms = ...  # type: Any
    save_m2m = ...  # type: Any
    def save(self, commit: bool = ...): ...
    def clean(self): ...
    def validate_unique(self): ...
    def get_unique_error_message(self, unique_check): ...
    def get_date_error_message(self, date_check): ...
    def get_form_error(self): ...
    changed_objects = ...  # type: Any
    deleted_objects = ...  # type: Any
    def save_existing_objects(self, commit: bool = ...): ...
    new_objects = ...  # type: Any
    def save_new_objects(self, commit: bool = ...): ...
    def add_fields(self, form, index): ...

def modelformset_factory(model, form: Any = ..., formfield_callback: Optional[Any] = ..., formset: Any = ..., extra: int = ..., can_delete: bool = ..., can_order: bool = ..., max_num: Optional[Any] = ..., fields: Optional[Any] = ..., exclude: Optional[Any] = ..., widgets: Optional[Any] = ..., validate_max: bool = ..., localized_fields: Optional[Any] = ..., labels: Optional[Any] = ..., help_texts: Optional[Any] = ..., error_messages: Optional[Any] = ..., min_num: Optional[Any] = ..., validate_min: bool = ..., field_classes: Optional[Any] = ...): ...

class BaseInlineFormSet(BaseModelFormSet):
    instance = ...  # type: Any
    save_as_new = ...  # type: Any
    unique_fields = ...  # type: Any
    def __init__(self, data: Optional[Any] = ..., files: Optional[Any] = ..., instance: Optional[Any] = ..., save_as_new: bool = ..., prefix: Optional[Any] = ..., queryset: Optional[Any] = ..., **kwargs) -> None: ...
    def initial_form_count(self): ...
    @classmethod
    def get_default_prefix(cls): ...
    def save_new(self, form, commit: bool = ...): ...
    def add_fields(self, form, index): ...
    def get_unique_error_message(self, unique_check): ...

def inlineformset_factory(parent_model, model, form: Any = ..., formset: Any = ..., fk_name: Optional[Any] = ..., fields: Optional[Any] = ..., exclude: Optional[Any] = ..., extra: int = ..., can_order: bool = ..., can_delete: bool = ..., max_num: Optional[Any] = ..., formfield_callback: Optional[Any] = ..., widgets: Optional[Any] = ..., validate_max: bool = ..., localized_fields: Optional[Any] = ..., labels: Optional[Any] = ..., help_texts: Optional[Any] = ..., error_messages: Optional[Any] = ..., min_num: Optional[Any] = ..., validate_min: bool = ..., field_classes: Optional[Any] = ...): ...

class InlineForeignKeyField(Field):
    widget = ...  # type: Any
    default_error_messages = ...  # type: Any
    parent_instance = ...  # type: Any
    pk_field = ...  # type: Any
    to_field = ...  # type: Any
    def __init__(self, parent_instance, *args, **kwargs) -> None: ...
    def clean(self, value): ...
    def has_changed(self, initial, data): ...

class ModelChoiceIterator:
    field = ...  # type: Any
    queryset = ...  # type: Any
    def __init__(self, field) -> None: ...
    def __iter__(self): ...
    def __len__(self): ...
    def choice(self, obj): ...

class ModelChoiceField(ChoiceField):
    default_error_messages = ...  # type: Any
    empty_label = ...  # type: Any
    queryset = ...  # type: Any
    limit_choices_to = ...  # type: Any
    to_field_name = ...  # type: Any
    def __init__(self, queryset, empty_label: str = ..., required: bool = ..., widget: Optional[Any] = ..., label: Optional[Any] = ..., initial: Optional[Any] = ..., help_text: str = ..., to_field_name: Optional[Any] = ..., limit_choices_to: Optional[Any] = ..., *args, **kwargs) -> None: ...
    def get_limit_choices_to(self): ...
    def __deepcopy__(self, memo): ...
    def label_from_instance(self, obj): ...
    choices = ...  # type: Any
    def prepare_value(self, value): ...
    def to_python(self, value): ...
    def validate(self, value): ...
    def has_changed(self, initial, data): ...

class ModelMultipleChoiceField(ModelChoiceField):
    widget = ...  # type: Any
    hidden_widget = ...  # type: Any
    default_error_messages = ...  # type: Any
    def __init__(self, queryset, required: bool = ..., widget: Optional[Any] = ..., label: Optional[Any] = ..., initial: Optional[Any] = ..., help_text: str = ..., *args, **kwargs) -> None: ...
    def to_python(self, value): ...
    def clean(self, value): ...
    def prepare_value(self, value): ...
    def has_changed(self, initial, data): ...
