from db.database import Database

db = Database()
db.create_table(
    "members",
    {"member_id": int, "name": str},
    primary_key="member_id"
)

# Insert rows
db.insert("members", {"member_id": 1, "name": "Mike"})
db.insert("members", {"member_id": 2, "name": "Kip"})

# Should fail
try:
    db.insert("members", {"member_id": 1, "name": "Billy"})
except ValueError as e:
    print("Error:", e)

# Print rows
table = db.get_table("members")
for r in table.rows:
    print(r)
