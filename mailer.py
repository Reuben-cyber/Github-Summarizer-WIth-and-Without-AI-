import smtplib
import os
from email.message import EmailMessage


def send_email(body):
    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_APP_PASSWORD")
    email_to = os.getenv("EMAIL_TO")

    if not gmail_user or not gmail_password or not email_to:
        raise ValueError("GMAIL_USER, GMAIL_APP_PASSWORD, or EMAIL_TO not set in .env")

    msg = EmailMessage()
    msg["Subject"] = "🚨 High Priority GitHub Issues"
    msg["From"] = gmail_user
    msg["To"] = email_to
    msg.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
