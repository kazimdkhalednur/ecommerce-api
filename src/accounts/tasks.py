from celery import Task, shared_task

from .mails import send_reset_mail, send_verification_mail


@shared_task
def send_reset_mail_task(user_id):
    send_reset_mail(user_id)


send_reset_mail_task: Task


@shared_task
def send_verification_mail_task(uidb64, user_mail, token, use_https, site_name, domain):
    send_verification_mail(uidb64, user_mail, token, use_https, site_name, domain)


send_verification_mail_task: Task
