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

    def select(self, columns=None, where=None):

        result = []

        for row in self.rows:
            match = True
            if where:
                for col, val in where.items():
                    if row.get(col) != val:
                        match = False
                        break
            if match:
                if columns:
                    result.append({col: row[col] for col in columns})
                else:
                    result.append(row.copy())

        return result
    
    def update(self, updates, where=None):

        updated_count = 0

        for row in self.rows:
            match = True
            if where:
                for col, val in where.items():
                    if row.get(col) != val:
                        match = False
                        break
            if match:
                # Enforce primary key update
                if self.primary_key and self.primary_key in updates:
                    new_pk = updates[self.primary_key]
                    old_pk = row[self.primary_key]
                    if new_pk != old_pk and new_pk in self.pk_index:
                        raise ValueError(f"Duplicate primary key '{new_pk}' in table '{self.name}'")
                    # Update index
                    self.pk_index.pop(old_pk)
                    self.pk_index[new_pk] = row

                # Update unique keys
                for key in self.unique_keys:
                    if key in updates:
                        new_val = updates[key]
                        old_val = row[key]
                        if new_val != old_val and new_val in self.unique_indexes[key]:
                            raise ValueError(f"Duplicate unique key '{new_val}' in table '{self.name}'")
                        self.unique_indexes[key].pop(old_val)
                        self.unique_indexes[key][new_val] = row

                # Apply updates
                for col, val in updates.items():
                    row[col] = val
                updated_count += 1

        return updated_count
    
    def delete(self, where=None):

        to_delete = []
        for row in self.rows:
            match = True
            if where:
                for col, val in where.items():
                    if row.get(col) != val:
                        match = False
                        break
            if match:
                to_delete.append(row)

        for row in to_delete:
            self.rows.remove(row)
            # Remove from indexes
            if self.primary_key:
                self.pk_index.pop(row[self.primary_key], None)
            for key in self.unique_keys:
                self.unique_indexes[key].pop(row[key], None)

        return len(to_delete)
