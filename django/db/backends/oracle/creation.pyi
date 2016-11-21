# Stubs for django.db.backends.oracle.creation (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.backends.base.creation import BaseDatabaseCreation

TEST_DATABASE_PREFIX = ...  # type: str

class DatabaseCreation(BaseDatabaseCreation):
    def set_as_test_mirror(self, primary_settings_dict): ...
    def test_db_signature(self): ...
