from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize with default data
current_data = [
    {'name': 'Alice', 'location': 'Office', 'status': 'Working', 'status_emoji': ''},
    {'name': 'Bob', 'location': 'Remote', 'status': 'Available', 'status_emoji': ''},
    {'name': 'Charlie', 'location': 'Meeting Room 5', 'status': 'In a meeting', 'status_emoji': ''}
    ]

@app.route('/')
def home():
    # Pass the current data to the template
    return render_template('display.html', team_info=current_data)

@app.route('/update', methods=['POST'])
def update_display():
    global current_data  # Refer to the global variable
    data = request.json
    print("Received data:", data)  # Debug print to check what data is received

    # Assuming the incoming data is structured as a list of dicts like the initial data
    current_data = data  # Replace the current data with the new data
    return jsonify({"success": True, "message": "Display updated successfully."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
