from typing import Any, TypeVar, Sequence, Tuple
from datetime import datetime

from django.db import models

UserT_co = TypeVar('UserT_co', covariant = True)

class BaseUserManager(models.Manager):
	
	@classmethod
	def normalize_email(cls, email: str) -> str: ...
	
	def make_random_password(self, length: int = ..., allowed_chars: str = ...) -> str: ...
	
	def get_by_natural_key(self, username: str) -> UserT_co: ...

class AbstractBaseUser(models.Model):
	password: str
	last_login: datetime
	
	is_active: bool
	REQUIRED_FIELDS: Sequence
	
	def __init__(self, *args: Any, **kwargs: Any) -> None: ...
	
	def __str__(self) -> str: ...
	
	def clean(self) -> None: ...
	
	def save(self, *args, **kwargs) -> None: ...
	
	def natural_key(self) -> Tuple[str]: ...
	
	@property
	def is_anonymous(self) -> bool: ...
	
	@property
	def is_authenticated(self) -> bool: ...
	
	def set_password(self, raw_password: str) -> None: ...
	
	def check_password(self, raw_password: str) -> bool: ...
	
	def set_unusable_password(self) -> None: ...
	
	def has_usable_password(self) -> bool: ...
	
	def get_full_name(self) -> str: ...
	
	def get_short_name(self) -> str: ...
	
	def get_session_auth_hash(self) -> str: ...
	
	@classmethod
	def normalize_username(cls, username: str) -> str: ...
	