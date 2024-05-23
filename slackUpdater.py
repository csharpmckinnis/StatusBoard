import time
from slack_sdk import WebClient
import requests
import emoji

slack_token = 'xoxb-5505935975286-7077443606788-AO5z8hBzZ6Voq1pHzbclDAFz'
client = WebClient(token=slack_token)

user_ids = ['UJMSXH0P5', 'ULX1SS2EA', 'U048W8THX6Y', 'U8PLW74GP']

def fetch_users_status():
    try:
        response = client.users_list()
        users_data = []
        for user in response['members']:
            if user['id'] in user_ids and not user['is_bot']:
                name = user['real_name']
                status_text = user.get('profile', {}).get('status_text', 'Available')
                status_emoji = user.get('profile', {}).get('status_emoji', '')
                title = user.get('profile', {}).get('title', 'No title provided')
                presence = 'Active' if user.get('presence') == 'active' else 'Inactive'
                profile_image = user.get('profile', {}).get('image_192', '')  # Gets 192x192 size image

    # Convert Slack emoji codes to Unicode
                full_status_text = f"{status_emoji} {status_text}"
                full_status = f"{emoji.emojize(full_status_text, language='alias')}"

                users_data.append({
                    'name': name,
                    'location': 'Remote',  # You might want to customize this if possible
                    'status': full_status,
                    'status_emoji': status_emoji,
                    'title': title,
                    'presence': presence,
                    'profile_image': profile_image
                })
        return users_data
    except Exception as e:
        print(f"Error fetching user data: {str(e)}")
        return None

def update_display(data):
    response = requests.post('http://localhost:8080/update', json=data)
    print(response.text)

if __name__ == '__main__':
    while True:
        user_status_data = fetch_users_status()
        if user_status_data:
            update_display(user_status_data)
        time.sleep(20)  # Wait for 60 seconds before the next run