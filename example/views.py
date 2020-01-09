from django.http import HttpResponse
from django.shortcuts import render

from .tasks import send_email_task


def index(request):
    send_email_task.delay()
    return HttpResponse('<h1>E-mail has been sent with celery!</h1>')
