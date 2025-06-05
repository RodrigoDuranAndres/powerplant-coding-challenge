from flask import Flask, request, jsonify
from utils.methods_advance import *
from utils.classes import *

app = Flask(__name__)

@app.route('/productionplan', methods=['POST'])
def dispatch():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    response = process_json(data)
    if "error" in response:
        return jsonify(response), 400
    try: 
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(port=8808)