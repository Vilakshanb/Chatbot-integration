import requests
from config import WATI_API_URL, WATI_BEARER_TOKEN
import requests

WATI_API_URL = "https://live-server-7354.wati.io"
WATI_BEARER_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIwMWRhYTQ1NC0yYzUwLTQ4NWYtYjA5NC03ZWMyYTYyOTcwNGUiLCJ1bmlxdWVfbmFtZSI6InZpbGFrc2hhbkBuaXZlc2hvbmxpbmUuY29tIiwibmFtZWlkIjoidmlsYWtzaGFuQG5pdmVzaG9ubGluZS5jb20iLCJlbWFpbCI6InZpbGFrc2hhbkBuaXZlc2hvbmxpbmUuY29tIiwiYXV0aF90aW1lIjoiMDgvMjkvMjAyMyAxMDowODoxNiIsImRiX25hbWUiOiI3MzU0IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiQURNSU5JU1RSQVRPUiIsImV4cCI6MjUzNDAyMzAwODAwLCJpc3MiOiJDbGFyZV9BSSIsImF1ZCI6IkNsYXJlX0FJIn0.VTuDjxHifaQ6FesKl9inIJD-UQwamsoEepgjbv0Ac3g"


def send_message(phone_number, message):
    try:
        endpoint = f"{WATI_API_URL}/sendTextMessage"
        headers = {"Authorization": WATI_BEARER_TOKEN}
        payload = {"phone": phone_number, "body": message}
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error sending message: {e}")
        return None


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
