from django.core.mail import send_mail
from django.conf import settings


def send_confirm_mail(email):
    subject = "Account Registration"
    message = 'Welcome'
    email_from = settings.EMAIL_HOST 
    
    send_mail(subject, message,email_from, [email])
    
    
    
    
# send_custom_mail    
# from django.core.mail import send_mail as django_send_mail
# from django.conf import settings

# def send_custom_mail(email):
#     subject = email.subject
#     message = email.message
#     email_from = settings.EMAIL_HOST 
    
#     django_send_mail(subject, message, email_from, [email])
# from django.core.mail import send_mail as django_send_mail
# from django.conf import settings

# def send_custom_mail(request, subject, message, email_addresses):
#     email_from = settings.EMAIL_HOST 
#     django_send_mail(subject, message, email_from, email_addresses)
