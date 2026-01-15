from flask import Blueprint, request, jsonify

accounts_bp = Blueprint("accounts", __name__)

db = None

def set_db(database):
    global db
    db = database

@accounts_bp.route("/accounts", methods=["POST"])
def add_account():
    data = request.json
    try:
        # Ensure member exists
        member_id = data.get("member_id")
        members = db.select("members", where={"member_id": member_id})
        if not members:
            return jsonify({"status": "error", "message": "Member not found"}), 404

        # Insert account
        db.insert("accounts", data)
        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# List accounts
@accounts_bp.route("/accounts", methods=["GET"])
def list_accounts():
    rows = db.select("accounts")
    return jsonify(rows)