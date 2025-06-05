from celery import shared_task

from django.conf import settings
from django.core.mail import EmailMessage


@shared_task(name="send mail")
def send_mail(subject, body, to_mail):
    from_email = settings.DEFAULT_FROM_EMAIL
    email = EmailMessage(
        subject=subject, body=body, from_email=from_email, to=[to_mail]
    )
    email.send(fail_silently=True)
    return True
