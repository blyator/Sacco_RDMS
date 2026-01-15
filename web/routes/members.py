from flask import Blueprint, request, jsonify

members_bp = Blueprint("members", __name__)


db = None
def set_db(database):
    global db
    db = database

# Add Member route
@members_bp.route("/members", methods=["POST"])
def add_member():
    data = request.json
    try:
        db.insert("members", data)
        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# List Members route
@members_bp.route("/members", methods=["GET"])
def list_members():
    rows = db.select("members")
    return jsonify(rows)
