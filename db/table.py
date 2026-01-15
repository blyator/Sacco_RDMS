class Table:
    def __init__(self, name, columns, primary_key=None, unique_keys=None):
        self.name = name
        self.columns = columns 
        self.primary_key = primary_key
        self.unique_keys = unique_keys or []
        self.rows = []
        self.pk_index = {}   
