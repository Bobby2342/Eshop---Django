# mail.py

from django.core.mail import send_mail

def send_custom_email(subject, message, email_from, recipient_list):
    """
    Function to send a custom email.
    """
    send_mail(subject, message, email_from, recipient_list)
