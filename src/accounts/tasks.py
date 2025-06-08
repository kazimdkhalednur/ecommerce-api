from celery import Task, shared_task

from .mails import send_reset_mail


@shared_task
def send_reset_mail_task(user_id):
    send_reset_mail(user_id)


send_reset_mail_task: Task
