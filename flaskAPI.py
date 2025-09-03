import json
import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PROCESSED_DATA_DIR = "./data/processed"

@app.route('/footballTeamsData/<string:country>', methods=['GET'])

def get_teams(country):
    file_name = f"{country}TeamsData.json"
    file_path = os.path.join(PROCESSED_DATA_DIR, file_name)

    if not os.path.exists(file_path):
        return jsonify({"error": "Country data not found"}), 404

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')

def index():
    return "API is running. Try to access /footballTeamsData/<country>."

if __name__ == "__main__":
    app.json.ensure_ascii = False
    app.run(debug=True, port=5000)