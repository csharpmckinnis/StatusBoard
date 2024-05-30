import time
from slack_sdk import WebClient
import requests
import emoji

# Slack token and client setup
slack_token = 'xoxb-5505935975286-7077443606788-AO5z8hBzZ6Voq1pHzbclDAFz'
client = WebClient(token=slack_token)

# List of user IDs to fetch statuses for
user_ids = ['UJMSXH0P5', 'ULX1SS2EA', 'U048W8THX6Y', 'U8PLW74GP']

def fetch_users_status():
    try:
        response = client.users_list()
        users_data = []
        for user in response['members']:
            if user['id'] in user_ids and not user['is_bot']:
                name = user['real_name']
                status_text = user.get('profile', {}).get('status_text', '')
                status_emoji = user.get('profile', {}).get('status_emoji', '')
                title = user.get('profile', {}).get('title', 'No title provided')
                profile_image = user.get('profile', {}).get('image_192', '/static/profile_placeholder.png')

                if not status_text:
                    status_text = 'Status not set'
                if not status_emoji:
                    status_emoji = ':no_entry:'
                    
                # Convert Slack emoji codes to Unicode
                full_status_text = f"{status_emoji} {status_text}".strip()
                full_status = emoji.emojize(full_status_text, language='alias')

                users_data.append({
                    'name': name,
                    'status': full_status,
                    'status_emoji': status_emoji,
                    'title': title,
                    'location': 'Updating...',  # Placeholder if location not provided by Slack
                    'profile_image': profile_image
                })
        return users_data
    except Exception as e:
        print(f"Error fetching user data: {str(e)}")
        return None
    except Exception as e:
        print(f"Error fetching user data: {str(e)}")
        return None

def update_display(data):
    try:
        response = requests.post('http://localhost:8080/update', json=data)
        print("Update response:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Failed to update display: {str(e)}")

if __name__ == '__main__':
    while True:
        user_status_data = fetch_users_status()
        if user_status_data:
            update_display(user_status_data)
        time.sleep(60)  # Adjust sleep time as necessary
