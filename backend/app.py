# app.py
import os
import json
from flask import Flask, jsonify, request
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)

# --- SOLUTION ---
# Updated CORS configuration to explicitly allow all origins for API routes.
# This tells the backend it's okay to accept requests from the frontend.
CORS(app, resources={r"/api/*": {"origins": "*"}})


# Define the path to the database file
DB_PATH = os.path.join(os.path.dirname(__file__), 'db.json')

def read_db():
    """Reads the data from the JSON database file."""
    try:
        with open(DB_PATH, 'r') as f:
            data = json.load(f)
            # Ensure the main keys exist
            if 'queued_volunteers' not in data:
                data['queued_volunteers'] = []
            if 'assigned_volunteers' not in data:
                data['assigned_volunteers'] = []
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is empty, return a default structure
        return {'queued_volunteers': [], 'assigned_volunteers': []}

def write_db(data):
    """Writes the given data to the JSON database file."""
    with open(DB_PATH, 'w') as f:
        json.dump(data, f, indent=2)

# --- API Endpoints ---

@app.route('/api/data', methods=['GET'])
def get_data():
    """Endpoint to fetch all queued and assigned volunteers."""
    data = read_db()
    return jsonify(data)

@app.route('/api/volunteers', methods=['POST'])
def add_volunteer():
    """Endpoint to add a new volunteer to the queue."""
    volunteer_data = request.get_json()

    if not all(k in volunteer_data for k in ['name', 'experienceYears', 'availabilityScore']):
        return jsonify({'message': 'Missing required volunteer data.'}), 400

    db_data = read_db()
    
    experience = float(volunteer_data['experienceYears'])
    availability = float(volunteer_data['availabilityScore'])
    
    new_volunteer = {
        'id': int(os.urandom(6).hex(), 16), # A simple unique ID
        'name': volunteer_data['name'],
        'experienceYears': experience,
        'availabilityScore': availability,
        'priority': (experience * 0.6) + (availability * 0.4)
    }

    db_data['queued_volunteers'].append(new_volunteer)
    write_db(db_data)

    return jsonify(new_volunteer), 201

@app.route('/api/assign', methods=['POST'])
def assign_volunteer():
    """Endpoint to assign the volunteer with the highest priority."""
    db_data = read_db()
    queued_volunteers = db_data.get('queued_volunteers', [])

    if not queued_volunteers:
        return jsonify({'message': 'No volunteers in the queue to assign.'}), 404

    # Find the volunteer with the highest priority
    highest_priority_volunteer = max(queued_volunteers, key=lambda v: v['priority'])
    
    # Remove from queued list and add to assigned list
    queued_volunteers.remove(highest_priority_volunteer)
    db_data.get('assigned_volunteers', []).insert(0, highest_priority_volunteer)

    write_db(db_data)

    return jsonify({
        'message': 'Successfully assigned volunteer.',
        'assignedVolunteer': highest_priority_volunteer
    })

# This block allows running the app directly with `python app.py`
if __name__ == '__main__':
    # The default port for Flask is 5000
    app.run(debug=True, port=5000)
