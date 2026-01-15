class Table:
    def __init__(self, name, columns, primary_key=None, unique_keys=None):
        self.name = name
        self.columns = columns 
        self.primary_key = primary_key
        self.unique_keys = unique_keys or []
        self.rows = []
        self.pk_index = {}   
        self.unique_indexes = {key: {} for key in self.unique_keys}

    def insert(self, row):
        # Check column names
        for col in row:
            if col not in self.columns:
                raise ValueError(f"Column '{col}' not in table '{self.name}'")

        # Enforce primary key
        if self.primary_key:
            pk_value = row.get(self.primary_key)
            if pk_value in self.pk_index:
                raise ValueError(f"Duplicate primary key '{pk_value}' in table '{self.name}'")
            self.pk_index[pk_value] = row

        # Enforce unique keys
        for key in self.unique_keys:
            val = row.get(key)
            if val in self.unique_indexes[key]:
                raise ValueError(f"Duplicate unique key '{val}' in table '{self.name}'")
            self.unique_indexes[key][val] = row
            
        self.rows.append(row)