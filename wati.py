import requests
from config import WATI_API_URL, WATI_BEARER_TOKEN


def send_message_to_user(phone_number, message):
    endpoint = f"{WATI_API_URL}/sendTextMessage"
    headers = {"Content-Type": "application/json", "Authorization": WATI_BEARER_TOKEN}
    payload = {"phone": phone_number, "body": message}

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        # Handle error scenarios
        return None


def listen_for_messages():
    # Pseudo-code: Replace with actual API call to Wati
    return "User's incoming message"
