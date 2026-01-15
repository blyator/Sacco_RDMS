from db.table import Table
from db.errors import TableExistsError, TableNotFoundError

class Database:
    def __init__(self):
        self.tables = {}

    def create_table(self, name, columns, primary_key=None, unique_keys=None):
        if name in self.tables:
            raise TableExistsError(f"Table '{name}' already exists")
        self.tables[name] = Table(name, columns, primary_key, unique_keys)

    def get_table(self, name):
        if name not in self.tables:
            raise TableNotFoundError(f"Table '{name}' not found")
        return self.tables[name]

    def insert(self, table_name, row):
        table = self.get_table(table_name)
        table.insert(row)