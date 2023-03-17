from monitoring.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def check_alarm(value):
    if value >= 126:
        send_email()
    return()

def send_email():
    subject = 'Test WIDMY'
    message = 'Warning!!! Paciente con glucosa muy alta'
    recepient = "azrael2402@gmail.com"
    send_mail(subject, message, EMAIL_HOST_USER, [recepient])