from time import sleep

from django.core.mail import send_mail

from celery import shared_task


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task():
    sleep(10)
    send_mail('Celery Task Worked!',
              'This is proof the task worked!',
              '<sender email>',
              ['<receiver e-mail>'])
    return None
