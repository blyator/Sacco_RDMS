from db.database import Database

db = Database()

def repl():
    print("Welcome to SACCO-RDBMS REPL. Type 'exit' to quit.")
    while True:
        cmd = input("> ").strip()
        if cmd.lower() in ("exit", "quit"):
            break
        if not cmd:
            continue
        try:
            execute(cmd)
        except Exception as e:
            print("Error:", e)

def execute(cmd):
    tokens = cmd.split()
    if tokens[0].upper() == "CREATE":
        #  parser for create table
        _, _, table_name, rest = tokens[0], tokens[1], tokens[2], " ".join(tokens[3:])
        rest = rest.strip("()")
        columns = {}
        primary_key = None
        for col_def in rest.split(","):
            parts = col_def.strip().split()
            col_name = parts[0]
            col_type = parts[1].upper()
            columns[col_name] = int if col_type == "INT" else str
            if "PRIMARY" in parts:
                primary_key = col_name
        db.create_table(table_name, columns, primary_key)
        print(f"Table '{table_name}' created.")

    elif tokens[0].upper() == "INSERT":
        # parser for insert into
        table_name = tokens[2]
        values_str = " ".join(tokens[4:]).strip("()")
        values = [v.strip("'") for v in values_str.split(",")]
        table = db.get_table(table_name)
        row = {}
        for col, val in zip(table.columns.keys(), values):
            if table.columns[col] == int:
                val = int(val)
            row[col] = val
        db.insert(table_name, row)
        print("Row inserted.")

    elif tokens[0].upper() == "SELECT":
        # parser for select
        cols_part = tokens[1]
        table_name = tokens[3]
        columns = None if cols_part == "*" else cols_part.split(",")
        rows = db.select(table_name, columns)
        for r in rows:
            print(r)

    elif tokens[0].upper() == "JOIN":
        # parser for join
        left_table = tokens[1]
        right_table = tokens[2]
        join_key = tokens[4]
        rows = db.join(left_table, right_table, join_key, join_key)
        for r in rows:
            print(r)

    else:
        print("Unknown command:", cmd)

if __name__ == "__main__":
    repl()
