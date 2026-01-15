from db.database import Database

db = Database()

# create tables 
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
