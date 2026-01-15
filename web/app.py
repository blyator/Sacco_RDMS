from flask import Flask
from db.instance import db
from .routes.members import members_bp, set_db as set_members_db
from .routes.accounts import accounts_bp, set_db as set_accounts_db
from .routes.transactions import transactions_bp, set_db as set_transactions_db
from .routes.sql import sql_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Inject DB 
set_members_db(db)
set_accounts_db(db)
set_transactions_db(db)

# Register blueprints
app.register_blueprint(members_bp)
app.register_blueprint(accounts_bp)
app.register_blueprint(transactions_bp)
app.register_blueprint(sql_bp)

if __name__ == "__main__":
    app.run(debug=True)
