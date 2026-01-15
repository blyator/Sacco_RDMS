import re
from db.instance import db 

print("Welcome to SACCO-RDBMS REPL. Type 'exit' to quit.")

while True:
    try:
        cmd = input("> ").strip()
        if cmd.lower() in ("exit", "quit"):
            break

        # ------------------- INSERT -------------------
        if cmd.upper().startswith("INSERT INTO"):
            m = re.match(r"INSERT INTO (\w+)\s*VALUES\s*\((.*)\)", cmd, re.I)
            if not m:
                print("Invalid INSERT syntax")
                continue
            table, values = m.groups()
            values = [v.strip().strip("'") for v in values.split(",")]
            for i, v in enumerate(values):
                if v.isdigit():
                    values[i] = int(v)
            columns = list(db.tables[table].columns.keys())
            data = dict(zip(columns, values))

            # handling for transactions
            if table.lower() == "transactions":
                account_id = data["account_id"]
                txn_type = data["txn_type"].lower()
                amount = data["amount"]

                accounts = db.select("accounts", where={"account_id": account_id})
                if not accounts:
                    print(f"Error: Account {account_id} not found")
                    continue

                account = accounts[0]

                if txn_type == "deposit":
                    account["balance"] += amount
                    db.update("accounts", {"balance": account["balance"]}, where={"account_id": account_id})
                    db.insert(table, data)
                    print(f"Deposit of {amount} to account {account_id} successful")
                elif txn_type == "withdraw":
                    if account["balance"] < amount:
                        print("Error: Insufficient balance")
                        continue
                    account["balance"] -= amount
                    db.update("accounts", {"balance": account["balance"]}, where={"account_id": account_id})
                    db.insert(table, data)
                    print(f"Withdrawal of {amount} from account {account_id} successful")
                else:
                    print("Error: txn_type must be 'deposit' or 'withdraw'")
            else:
                db.insert(table, data)
                print(f"{table} row inserted successfully")

        # ------------------- SELECT -------------------
        elif cmd.upper().startswith("SELECT"):
            m = re.match(r"SELECT \* FROM (\w+)(?: WHERE (.*))?", cmd, re.I)
            if not m:
                print("Invalid SELECT syntax")
                continue
            table, where_clause = m.groups()
            where = {}
            if where_clause:
                key, val = [x.strip() for x in where_clause.split("=")]
                val = val.strip("'")
                if val.isdigit():
                    val = int(val)
                where[key] = val
            rows = db.select(table, where=where if where else None)
            print(rows)

        # ------------------- UPDATE -------------------
        elif cmd.upper().startswith("UPDATE"):
            m = re.match(r"UPDATE (\w+) SET (.*) WHERE (.*)", cmd, re.I)
            if not m:
                print("Invalid UPDATE syntax")
                continue
            table, set_clause, where_clause = m.groups()
            set_key, set_val = [x.strip() for x in set_clause.split("=")]
            set_val = set_val.strip("'")
            if set_val.isdigit():
                set_val = int(set_val)
            where_key, where_val = [x.strip() for x in where_clause.split("=")]
            where_val = where_val.strip("'")
            if where_val.isdigit():
                where_val = int(where_val)
            db.update(table, {set_key: set_val}, where={where_key: where_val})
            print(f"{table} row(s) updated successfully")

        # ------------------- DELETE -------------------
        elif cmd.upper().startswith("DELETE FROM"):
                m = re.match(r"DELETE FROM (\w+)\s+WHERE\s+(.*)", cmd, re.I)
                if not m:
                    print("Invalid DELETE syntax")
                    continue
                table, where_clause = m.groups()
                key, val = [x.strip() for x in where_clause.split("=")]
                val = val.strip("'")
                if val.isdigit():
                    val = int(val)
                deleted_count = db.delete(table, where={key: val})
                print(f"{deleted_count} row(s) deleted from {table}")

        else:
            print("Unknown command")

    except Exception as e:
        print(f"Error: {e}")
