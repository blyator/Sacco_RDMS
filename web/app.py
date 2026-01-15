from flask import Flask
from db.database import Database
from .routes.members import members_bp, set_db as set_members_db



app = Flask(__name__)

# Custom RDBMS
db = Database()

# Setup SACCO members table
db.create_table(
    "members",
    {"member_id": int, "name": str, "national_id": str},
    primary_key="member_id",
    unique_keys=["national_id"]
)

set_members_db(db)

# Register blueprint
app.register_blueprint(members_bp)

if __name__ == "__main__":
    app.run(debug=True)
