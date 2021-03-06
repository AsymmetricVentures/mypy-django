# Stubs for django.core.mail (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.core.mail.message import DEFAULT_ATTACHMENT_MIME_TYPE as DEFAULT_ATTACHMENT_MIME_TYPE, BadHeaderError as BadHeaderError, EmailMessage as EmailMessage, EmailMultiAlternatives as EmailMultiAlternatives, SafeMIMEMultipart as SafeMIMEMultipart, SafeMIMEText as SafeMIMEText, forbid_multi_line_headers as forbid_multi_line_headers, make_msgid as make_msgid
from django.core.mail.utils import DNS_NAME as DNS_NAME, CachedDnsName as CachedDnsName

def get_connection(backend: Optional[Any] = ..., fail_silently: bool = ..., **kwds): ...
def send_mail(subject, message, from_email, recipient_list, fail_silently: bool = ..., auth_user: Optional[Any] = ..., auth_password: Optional[Any] = ..., connection: Optional[Any] = ..., html_message: Optional[Any] = ...): ...
def send_mass_mail(datatuple, fail_silently: bool = ..., auth_user: Optional[Any] = ..., auth_password: Optional[Any] = ..., connection: Optional[Any] = ...): ...
def mail_admins(subject, message, fail_silently: bool = ..., connection: Optional[Any] = ..., html_message: Optional[Any] = ...): ...
def mail_managers(subject, message, fail_silently: bool = ..., connection: Optional[Any] = ..., html_message: Optional[Any] = ...): ...
