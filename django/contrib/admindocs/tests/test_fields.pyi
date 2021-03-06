# Stubs for django.contrib.admindocs.tests.test_fields (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import models
import unittest
from django.utils.translation import ugettext as _

class CustomField(models.Field):
    description = ...  # type: str

class DescriptionLackingField(models.Field): ...

class TestFieldType(unittest.TestCase):
    def setUp(self): ...
    def test_field_name(self): ...
    def test_builtin_fields(self): ...
    def test_custom_fields(self): ...
