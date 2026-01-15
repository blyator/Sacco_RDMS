from db.database import Database

db = Database()
db.create_table(
    "members",
    {"member_id": int, "name": str},
    primary_key="member_id"
)

db.insert("members", {"member_id": 1, "name": "Mike"})
db.insert("members", {"member_id": 2, "name": "kip"})


print("Update kip -> Billy")
db.update("members", {"name": "Billy"}, where={"name": "kip"})
for r in db.select("members"):
    print(r)