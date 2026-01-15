import re
from db.instance import db 

def execute_command(cmd):

    try:
        cmd = cmd.strip()
        
        # ------------------- INSERT -------------------
        if cmd.upper().startswith("INSERT INTO"):
            m = re.match(r"INSERT INTO (\w+)\s*VALUES\s*\((.*)\)", cmd, re.I)
            if not m:
                return {"status": "error", "message": "Invalid INSERT syntax"}
            
            table, values = m.groups()
            values = [v.strip().strip("'") for v in values.split(",")]
            for i, v in enumerate(values):
                if v.isdigit():
                    values[i] = int(v)
            
            if table not in db.tables:
                return {"status": "error", "message": f"Table '{table}' not found"}

            columns = list(db.tables[table].columns.keys())
            if len(values) != len(columns):
                 return {"status": "error", "message": f"Column count mismatch. Expected {len(columns)}, got {len(values)}"}

            data = dict(zip(columns, values))

            # handling for transactions
            if table.lower() == "transactions":
                account_id = data.get("account_id")
                txn_type = data.get("txn_type", "").lower()
                amount = data.get("amount", 0)

                accounts = db.select("accounts", where={"account_id": account_id})
                if not accounts:
                    return {"status": "error", "message": f"Error: Account {account_id} not found"}

                account = accounts[0]

                if txn_type == "deposit":
                    account["balance"] += amount
                    db.update("accounts", {"balance": account["balance"]}, where={"account_id": account_id})
                    db.insert(table, data)
                    return {"status": "success", "message": f"Deposit of {amount} to account {account_id} successful", "data": data}
                elif txn_type == "withdraw":
                    if account["balance"] < amount:
                        return {"status": "error", "message": "Error: Insufficient balance"}
                    account["balance"] -= amount
                    db.update("accounts", {"balance": account["balance"]}, where={"account_id": account_id})
                    db.insert(table, data)
                    return {"status": "success", "message": f"Withdrawal of {amount} from account {account_id} successful", "data": data}
                else:
                    return {"status": "error", "message": "Error: txn_type must be 'deposit' or 'withdraw'"}
            else:
                db.insert(table, data)
                return {"status": "success", "message": f"{table} row inserted successfully", "data": data}

        # ------------------- SELECT -------------------
        elif cmd.upper().startswith("SELECT"):
            m = re.match(r"SELECT \* FROM (\w+)(?: WHERE (.*))?", cmd, re.I)
            if not m:
                return {"status": "error", "message": "Invalid SELECT syntax"}
            
            table, where_clause = m.groups()
            where = {}
            if where_clause:
                parts = [x.strip() for x in where_clause.split("=")]
                if len(parts) == 2:
                    key, val = parts
                    val = val.strip("'")
                    if val.isdigit():
                        val = int(val)
                    where[key] = val
            
            try:
                rows = db.select(table, where=where if where else None)
                return {"status": "success", "data": rows}
            except Exception as e:
                return {"status": "error", "message": str(e)}

        # ------------------- UPDATE -------------------
        elif cmd.upper().startswith("UPDATE"):
            m = re.match(r"UPDATE (\w+) SET (.*) WHERE (.*)", cmd, re.I)
            if not m:
                return {"status": "error", "message": "Invalid UPDATE syntax"}
            
            table, set_clause, where_clause = m.groups()
            
            set_parts = [x.strip() for x in set_clause.split("=")]
            if len(set_parts) != 2: return {"status": "error", "message": "Invalid SET syntax"}
            set_key, set_val = set_parts
            set_val = set_val.strip("'")
            if set_val.isdigit(): set_val = int(set_val)
            
            where_parts = [x.strip() for x in where_clause.split("=")]
            if len(where_parts) != 2: return {"status": "error", "message": "Invalid WHERE syntax"}
            where_key, where_val = where_parts
            where_val = where_val.strip("'")
            if where_val.isdigit(): where_val = int(where_val)
            
            try:
                db.update(table, {set_key: set_val}, where={where_key: where_val})
                return {"status": "success", "message": f"{table} updated successfully"}
            except Exception as e:
                 return {"status": "error", "message": str(e)}

        # ------------------- DELETE -------------------
        elif cmd.upper().startswith("DELETE FROM"):
                m = re.match(r"DELETE FROM (\w+)\s+WHERE\s+(.*)", cmd, re.I)
                if not m:
                    return {"status": "error", "message": "Invalid DELETE syntax"}
                
                table, where_clause = m.groups()
                parts = [x.strip() for x in where_clause.split("=")]
                if len(parts) != 2: return {"status": "error", "message": "Invalid WHERE syntax"}
                key, val = parts
                val = val.strip("'")
                if val.isdigit():
                    val = int(val)
                
                try:
                    deleted_count = db.delete(table, where={key: val})
                    return {"status": "success", "message": f"{deleted_count} row(s) deleted from {table}"}
                except Exception as e:
                    return {"status": "error", "message": str(e)}

        else:
            return {"status": "error", "message": "Unknown command"}

    except Exception as e:
        return {"status": "error", "message": str(e)}

# Interactive REPL
if __name__ == "__main__":
    print("Welcome to SACCO-RDBMS REPL. Type 'exit' to quit.")
    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() in ("exit", "quit"):
                break
            
            result = execute_command(user_input)
            
            if result["status"] == "success":
                if "data" in result:
                    print(result["data"])
                else:
                    print(result["message"])
            else:
                print(f"Error: {result['message']}")
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")