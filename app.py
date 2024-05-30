from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy data - initial
people = [
    {'name': 'Alice', 'location': 'Office', 'status': 'Working', 'status_emoji': '🏢', 'profile_image': '/static/profile_placeholder.png'},
    {'name': 'Bob', 'location': 'Remote', 'status': 'Available', 'status_emoji': '🏠', 'profile_image': '/static/profile_placeholder.png'},
    {'name': 'Charlie', 'location': 'Meeting Room 5', 'status': 'In a meeting', 'status_emoji': '📅', 'profile_image': '/static/profile_placeholder.png'},
    {'name': 'Dana', 'location': 'Out of Office', 'status': 'Out of Office', 'status_emoji': '🏠', 'profile_image': '/static/profile_placeholder.png'}
]

announcements = [""]  # Use an equals sign to initialize the list

@app.route('/')
def status_board():
    global people, announcements  # Include both people and announcements
    return render_template('display.html', people=people, announcements=announcements)

@app.route('/update', methods=['POST'])
def update_status():
    global people
    people = request.json
    return jsonify({"status": "success"}), 200
    
@app.route('/data', methods=['GET'])
def get_data():
    global people
    return jsonify(people)
    
@app.route('/announce', methods=['POST'])
def announce():
    global announcements
    announcement = request.json.get('announcement')
    if announcement:
        announcements[0]=announcement
    return jsonify({"status": "success"}), 200
    
@app.route('/announcements', methods=['GET'])
def get_announcements():
    global announcements
    return jsonify(announcements)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
