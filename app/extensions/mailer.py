import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_babel import Locale

from ..settings import SMTP_PASSWORD, SMTP_USERNAME

# Define sender and recipient email addresses
sender_email = SMTP_USERNAME
recipient_email = sender_email

smtp_server = "smtp.gmail.com"
smtp_port = 587

password = SMTP_PASSWORD

if password=='': print("Warning! SMTP password unset!")

# This isn't translated because it is for the admin
def new_user(user):
    if password=='':
        print('Can not send new user mail, no password!')
        return

    # Create the message object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = "New User"

    # Add the message body
    body = f"""Hi Eric,

    A new user Just registered.
    - Name: {user.name}
    - Email: {user.email}
    - Language: {Locale(user.lang).display_name.capitalize()}

    Activate it or edit it through this link:
    https://navlab.ericroy.net/users/{user.id}/edit"""
    message.attach(MIMEText(body, 'plain'))

    # Connect to Gmail's SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("New user email sent successfully!")
