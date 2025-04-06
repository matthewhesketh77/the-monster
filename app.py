from flask import Flask, jsonify, request
from main_loop import log_cycle, self_reflection

app = Flask(__name__)

# Simple route to view the status of The Monster
@app.route('/')
def index():
    return "Welcome to The Monster's Web Interface!"

# Route to trigger self-reflection and re-prioritize goals
@app.route('/self_reflection', methods=['POST'])
def trigger_reflection():
    try:
        self_reflection()  # Calls the self_reflection function
        return jsonify({"status": "Reflection triggered successfully!"}), 200
    except Exception as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500

# Route to trigger goal generation
@app.route('/generate_goals', methods=['POST'])
def generate_goals():
    try:
        subprocess.run(["python3", "generate_goals.py"])  # Trigger goal generation
        return jsonify({"status": "Goals generated successfully!"}), 200
    except Exception as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500

# Route to get the current log entries
@app.route('/logs', methods=['GET'])
def get_logs():
    try:
        with open('log.json', 'r') as f:
            logs = json.load(f)
        return jsonify(logs), 200
    except FileNotFoundError:
        return jsonify({"status": "Log file not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)

