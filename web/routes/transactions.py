from flask import Blueprint, request, jsonify

transactions_bp = Blueprint("transactions", __name__)

db = None

def set_db(database):
    global db
    db = database

@transactions_bp.route("/transactions", methods=["POST"])
def add_transaction():
    data = request.json
    try:
        account_id = data.get("account_id")
        txn_type = data.get("txn_type")
        amount = data.get("amount")
        txn_id = data.get("txn_id")

        # Check account exists
        accounts = db.select("accounts", where={"account_id": account_id})
        if not accounts:
            return jsonify({"status": "error", "message": "Account not found"}), 404

        # Update balance
        account = accounts[0]
        if txn_type == "deposit":
            account["balance"] += amount
        elif txn_type == "withdraw":
            if account["balance"] < amount:
                return jsonify({"status": "error", "message": "Insufficient balance"}), 400
            account["balance"] -= amount
        else:
            return jsonify({"status": "error", "message": "Invalid txn_type"}), 400

        db.update("accounts", {"balance": account["balance"]}, where={"account_id": account_id})

        # Record transaction
        db.insert("transactions", {"txn_id": txn_id, "account_id": account_id, "amount": amount, "txn_type": txn_type})

        return jsonify({"status": "success"}), 201

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    
@transactions_bp.route("/transactions", methods=["GET"])
def list_transactions():
    rows = db.select("transactions")
    return jsonify(rows)
