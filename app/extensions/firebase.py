import google.auth.transport.requests
from google.oauth2 import service_account
import json, requests
from ..settings import GOOGLE_AUTH_FILE_ABSOLUTE_PATH
from ..models import FirebaseToken, User
from ..extensions import db

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

def send_to_admins(title, message):
    fts = FirebaseToken.query.join(FirebaseToken, FirebaseToken.user_id == User.id).filter(User.admin == True).all()
    if len(fts) == 0: return

    server_token = get_bearer_token()
    for ft in fts:
        client_token = ft.token
        r = send_notification(title, message, client_token, server_token)
        if not r: # Failed to deliver notification, remove FT.
            db.session.delete(ft)

    db.session.commit()

def notify_new_user(new_user):
    User.send_to_admins("New User", f"User {new_user.name} just landed, activate their account!")

def notify_server_started(server, user):
    User.send_to_admins("Server started", f"Server {server.name} been just started by {user.name}.")

def notify_server_stopped(server, user):
    User.send_to_admins("Server stopped", f"Server {server.name} been just stopped by {user.name}.")
