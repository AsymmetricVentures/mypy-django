# Stubs for django.db.backends.sqlite3.creation (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.backends.base.creation import BaseDatabaseCreation

class DatabaseCreation(BaseDatabaseCreation):
    def get_test_db_clone_settings(self, number): ...
    def test_db_signature(self): ...
