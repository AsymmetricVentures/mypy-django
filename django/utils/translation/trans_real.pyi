# Stubs for django.utils.translation.trans_real (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import gettext_module

CONTEXT_SEPARATOR = ...  # type: str
accept_language_re = ...  # type: Any
language_code_re = ...  # type: Any
language_code_prefix_re = ...  # type: Any

def reset_cache(**kwargs): ...
def to_locale(language, to_lower: bool = ...): ...
def to_language(locale): ...

class DjangoTranslation(gettext_module.GNUTranslations):
    domain = ...  # type: str
    def __init__(self, language, domain: Optional[Any] = ..., localedirs: Optional[Any] = ...) -> None: ...
    plural = ...  # type: Any
    def merge(self, other): ...
    def language(self): ...
    def to_language(self): ...

def translation(language): ...
def activate(language): ...
def deactivate(): ...
def deactivate_all(): ...
def get_language(): ...
def get_language_bidi(): ...
def catalog(): ...
def do_translate(message, translation_function): ...
def gettext(message): ...

ugettext = ...  # type: Any

def pgettext(context, message): ...
def gettext_noop(message): ...
def do_ntranslate(singular, plural, number, translation_function): ...
def ngettext(singular, plural, number): ...

ungettext = ...  # type: Any

def npgettext(context, singular, plural, number): ...
def all_locale_paths(): ...
def check_for_language(lang_code): ...
def get_languages(): ...
def get_supported_language_variant(lang_code, strict: bool = ...): ...
def get_language_from_path(path, strict: bool = ...): ...
def get_language_from_request(request, check_path: bool = ...): ...

dot_re = ...  # type: Any

def blankout(src, char): ...

context_re = ...  # type: Any
inline_re = ...  # type: Any
block_re = ...  # type: Any
endblock_re = ...  # type: Any
plural_re = ...  # type: Any
constant_re = ...  # type: Any

def templatize(src, origin: Optional[Any] = ...): ...
def parse_accept_lang_header(lang_string): ...