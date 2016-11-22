# Stubs for django.db.models (Python 3.6)

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import signals as signals
from django.db.models.aggregates import *
from django.db.models.deletion import (
    CASCADE as CASCADE, DO_NOTHING as DO_NOTHING, PROTECT as PROTECT, SET as SET, SET_DEFAULT as SET_DEFAULT, SET_NULL as SET_NULL, ProtectedError,
)
from django.db.models.expressions import (
    Case as Case, Expression as Expression, ExpressionWrapper as ExpressionWrapper, F as F, Func as Func, Value as Value, When as When,
)
from django.db.models.fields import *  
from django.db.models.fields.files import FileField as FileField, ImageField as ImageField
from django.db.models.fields.proxy import OrderWrt
from django.db.models.lookups import Lookup as Lookup, Transform as Transform
from django.db.models.manager import Manager as Manager
from django.db.models.query import (
    Prefetch as Prefetch, Q as Q, QuerySet as QuerySet, prefetch_related_objects,
)

# Imports that would create circular imports if sorted
from django.db.models.base import DEFERRED as DEFERRED, Model as Model
from django.db.models.fields.related import (
    ForeignKey as ForeignKey, ForeignObject, OneToOneField as OneToOneField, ManyToManyField as ManyToManyField,
    ManyToOneRel as ManyToOneRel, ManyToManyRel as ManyToManyRel, OneToOneRel as OneToOneRel,
)

def permalink(func): ...
