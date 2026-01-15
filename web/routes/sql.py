from flask import Blueprint, request, jsonify
from db.repl import execute_command

sql_bp = Blueprint('sql', __name__)

@sql_bp.route('/sql', methods=['POST', 'OPTIONS'])
def execute_sql():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200

    data = request.get_json()
    cmd = data.get('query', '').strip()
    
    if not cmd:
        return jsonify({"message": "Empty query"}), 400

    result = execute_command(cmd)

    if result["status"] == "success":
        # Check if it's a SELECT 
        response_data = result.get("data") if "data" in result else result.get("message")
        return jsonify(response_data)
    else:
        return jsonify({"message": result["message"]}), 400
