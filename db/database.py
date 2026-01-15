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

    def select(self, table_name, columns=None, where=None):
        table = self.get_table(table_name)
        return table.select(columns=columns, where=where)
    
    def update(self, table_name, updates, where=None):
        table = self.get_table(table_name)
        return table.update(updates, where=where)
    
    def delete(self, table_name, where=None):
        table = self.get_table(table_name)
        return table.delete(where=where)
    
# Method to perform JOIN operations
    def join(self, left_table_name, right_table_name, left_key, right_key, columns=None):

        left_table = self.get_table(left_table_name)
        right_table = self.get_table(right_table_name)

        result = []

        # Build hash map for efficiency
        right_index = {}
        for row in right_table.rows:
            key = row[right_key]
            right_index.setdefault(key, []).append(row)

        for l_row in left_table.rows:
            l_value = l_row[left_key]
            r_rows = right_index.get(l_value, [])
            for r_row in r_rows:
                combined = {**l_row, **r_row}
                if columns:
                    result.append({col: combined[col] for col in columns})
                else:
                    result.append(combined)
        return result
