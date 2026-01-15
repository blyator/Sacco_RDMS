from flask import Flask
from db.database import Database
from .routes.members import members_bp, set_db as set_members_db
from .routes.accounts import accounts_bp, set_db as set_accounts_db
from .routes.transactions import transactions_bp, set_db as set_transactions_db

app = Flask(__name__)

# Custom RDBMS
db = Database()

# SACCO members table
db.create_table(
    "members",
    {"member_id": int, "name": str, "national_id": str},
    primary_key="member_id",
    unique_keys=["national_id"]
)

db.create_table(
    "accounts",
    {"account_id": int, "member_id": int, "balance": int},
    primary_key="account_id"
)

db.create_table(
    "transactions",
    {"txn_id": int, "account_id": int, "amount": int, "txn_type": str},
    primary_key="txn_id"
)



set_members_db(db)
set_accounts_db(db)
set_transactions_db(db)


app.register_blueprint(members_bp)
app.register_blueprint(accounts_bp)
app.register_blueprint(transactions_bp)

if __name__ == "__main__":
    app.run(debug=True)
