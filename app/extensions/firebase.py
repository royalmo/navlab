import google.auth.transport.requests
from google.oauth2 import service_account
import json, requests
from ..settings import GOOGLE_AUTH_FILE_ABSOLUTE_PATH

if GOOGLE_AUTH_FILE_ABSOLUTE_PATH == '':
    print("Warning: firebase credentials are not set!")

def get_bearer_token():
    if GOOGLE_AUTH_FILE_ABSOLUTE_PATH == '': return '' # Preventing errors

    credentials = service_account.Credentials.from_service_account_file(
      GOOGLE_AUTH_FILE_ABSOLUTE_PATH,
      scopes=['https://www.googleapis.com/auth/firebase.messaging'])
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)

    return credentials.token

def send_notification(title, message, client_token, server_token):
    # In case of unset credentials we return True because if not FT get deleted.
    if GOOGLE_AUTH_FILE_ABSOLUTE_PATH == '': return True

    url = "https://fcm.googleapis.com/v1/projects/navlab-36618/messages:send"

    headers = {
        "Authorization": f"Bearer {server_token}",
        "Content-Type": "application/json"
    }

    data = {
        "message": {
            "token": client_token,
            "notification": {
                "title": title,
                "body": message
            },
            "data": {}
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.ok
