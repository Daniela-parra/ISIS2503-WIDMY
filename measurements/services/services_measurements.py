from monitoring.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def check_alarm(value):
    if value >= 126:
        send_email()
    return()

def check_alarm_Peso(value):
    if value >= 70:
        send_email_Peso()
    return()

def check_alarm_Temperatura(value):
    if value >= 38:
        send_email_Temperatura()
    return()

def send_email():
    subject = 'Test WIDMY'
    message = 'Warning!!! Paciente con glucosa muy alta'
    recepient = "azrael2402@gmail.com"
    send_mail(subject, message, EMAIL_HOST_USER, [recepient])

def send_email_Peso():
    subject = 'Test WIDMY'
    message = 'Warning!!! Paciente con peso muy alto'
    recepient = "azrael2402@gmail.com"
    send_mail(subject, message, EMAIL_HOST_USER, [recepient])

def send_email_Temperatura():
    subject = 'Test WIDMY'
    message = 'Warning!!! Paciente con temperatura muy alta'
    recepient = "azrael2402@gmail.com"
    send_mail(subject, message, EMAIL_HOST_USER, [recepient])