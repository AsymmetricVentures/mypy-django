from typing import Any, List, Tuple, Sequence, Type, Set, Optional
from datetime import datetime

from django.db import models

from .base_user import UserT_co, BaseUserManager, AbstractBaseUser

def update_last_login(sender, user, **kwargs): ...

class PermissionManager(models.Manager):
	use_in_migrations = ... # type: bool
	
	def get_by_natural_key(self, codename: str, app_label: str, model: Any) -> Permission: ...

class Permission(models.Model):
	name: str
	content_type: models.ForeignKey
	codename: str
	# TODO: with python 3.6b4, ClassVar has been added to `typing`
	objects: ClassVar[PermissionManager] # type: ignore
	
	class Meta:
		verbose_name: str
		verbose_name_plural: str
		unique_together: Sequence[Tuple[str, str]]
		ordering: Sequence[str]
	
	def __str__(self) -> str: ...
	
	def natural_key(self) -> Tuple[str]: ...

class GroupManager(models.Manager):
	use_in_migations: bool
	
	def get_by_natural_key(self, name: str) -> Group: ...

class Group(models.Model):
	name: str
	permissions: models.ManyToManyField
	objects: ClassVar[GroupManager] # type: ignore
	
	class Meta:
		verbose_name: str
		verbose_name_plural: str
	
	def __str__(self) -> str: ...
	
	def natural_key(self) -> Tuple[str]: ...

class UserManager(BaseUserManager):
	use_in_migrations: bool
	
	def _create_user(self, username: str, email: str, password: str, **extra_fields: Any) -> Type[UserT_co]: ...
	
	def create_user(self, username: str, email: Optional[str] = ..., password: Optional[str] = ..., **extra_fiels: Any) -> Type[UserT_co]: ...
	
	def create_superuser(self, username: str, email: str, password: str, **extra_fields: Any) -> Type[UserT_co]: ...

def _user_get_all_permissions(user: Type[UserT_co], obj: Any) -> Set[Permission]: ...

def _user_has_perm(user: Type[UserT_co], perm: Permission, obj: Any) -> bool: ...

def _user_has_module_perms(user: Type[UserT_co], app_label: str) -> bool: ...

class PermissionsMixin(models.Model):
	is_superuser: bool
	groups: models.ManyToManyField
	user_permission: models.ManyToManyField
	
	class Meta:
		abstract: bool
	
	def get_group_permissions(self, obj: Optional[Any] = ...) -> Set[Permission]: ...
	
	def has_perm(self, obj: Optional[Any] = ...) -> bool: ...
	
	def has_perms(self, perm_list: Sequence[Any], obj: Optional[Any] = ...) -> bool: ...
	
	def has_module_perms(self, app_label: str) -> bool: ...

class AbstractUser(AbstractBaseUser, PermissionsMixin):
	username_validator: ClassVar[Any] # type: ignore
	username: str
	first_name: str
	last_name: str
	email: str
	is_staff: bool
	is_active: bool
	date_joined: datetime
	objects: ClassVar[UserManager] # type: ignore
	
	USERNAME_FIELD: ClassVar[str] # type: ignore
	REQUIRED_FIELDS: ClassVar[Sequence[str]] #type: ignore
	
	class Meta:
		verbose_name: str
		verbose_name_plural: str
		abstract: bool
	
	def get_full_name(self) -> str: ...
	def get_short_name(self) -> str: ...
	def email_user(self, subject: str, message: str, from_email: Optional[str] = ..., **kwargs: Any) -> None: ...

class User(AbstractUser): ...

class AnonymousUser:
	id: Optional[int]
	pk: Optional[int]
	username: str
	is_staff: bool
	is_active: bool
	is_superuser: bool
	
