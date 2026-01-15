from flask import Flask
from db.database import Database
from .routes.members import members_bp, set_db as set_members_db
from .routes.accounts import accounts_bp, set_db as set_accounts_db

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


set_members_db(db)
set_accounts_db(db)


app.register_blueprint(members_bp)
app.register_blueprint(accounts_bp)


if __name__ == "__main__":
    app.run(debug=True)
