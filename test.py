from db.database import Database

db = Database()

db.create_table("members", {"member_id": int, "name": str}, primary_key="member_id")
db.create_table("accounts", {"account_id": int, "member_id": int, "balance": int}, primary_key="account_id")


db.insert("members", {"member_id": 1, "name": "Mike"})
db.insert("members", {"member_id": 2, "name": "Kip"})

db.insert("accounts", {"account_id": 1, "member_id": 1, "balance": 500})
db.insert("accounts", {"account_id": 2, "member_id": 2, "balance": 1000})

# Join members with accounts
print("Members with Accounts:")
for r in db.join("members", "accounts", "member_id", "member_id"):
    print(r)

# Join with selected columns
print("\nNames and Balances:")
for r in db.join("members", "accounts", "member_id", "member_id", columns=["name", "balance"]):
    print(r)