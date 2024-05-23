import requests

def send_update(data):
    url = 'http://localhost:8080/update'  # Change to your Flask app's URL if different
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=data, headers=headers)
    return response.json()

if __name__ == '__main__':
    # Example data to send
    data = [
        {
        'name': 'Alice',
        'title': 'Project Manager',
        'location': 'Remote',
        'status': 'Online'
        },
        {
        'name': 'Charles',
        'title': 'Intern',
        'location': 'Collab Space',
        'status': 'Active'
        }
    ]

    result = send_update(data)
    print("Response from server:", result)
