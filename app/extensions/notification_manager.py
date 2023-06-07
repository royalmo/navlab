from .firebase import get_bearer_token, send_notification
from .db import db

def send_to_admins(title, message):
    # Importing it here so it doesn't give circular import error.
    from ..models import FirebaseToken, User

    fts = db.session.query(FirebaseToken).join(User, User.id == FirebaseToken.user_id).filter(User.admin == True).all()
    if len(fts) == 0: return

    server_token = get_bearer_token()
    for ft in fts:
        client_token = ft.token
        r = send_notification(title, message, client_token, server_token)
        if not r: # Failed to deliver notification, remove FT.
            db.session.delete(ft)

    db.session.commit()

def notify_new_user(new_user):
    send_to_admins("New User", f"User {new_user.name} just landed, activate their account!")

def notify_server_started(server, user):
    send_to_admins("Server started", f"Server {server.name} been just started by {user.name}.")

def notify_server_stopped(server, user):
    send_to_admins("Server stopped", f"Server {server.name} been just stopped by {user.name}.")
