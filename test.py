from db.database import Database

db = Database()
db.create_table(
    "members",
    {"member_id": int, "name": str},
    primary_key="member_id"
)

print(db.tables.keys())
