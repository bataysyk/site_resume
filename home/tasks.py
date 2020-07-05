from celery import shared_task

from django.core.mail import send_mail

from time import sleep


#@shared_task
#def sleepy(duration):
#    sleep(duration)
#    return None


@shared_task
def send_email_task():
    send_mail('Celery Task Worked!',
    'This is proof the task worked!',
    'bataysk55@gmail.com',
    ['bataysk55@gmail.com'])
    print("Message send on email bataysk55@gmail.com")
    return None

@shared_task
def prints():
    print("WORKED")
    return "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"

@shared_task
def send_email_task_2():
    send_mail('Celery Task Worked!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    'This is proof the task worked!',
    'bataysk55@gmail.com',
    ['bataysk55@gmail.com'])
    print("Message send on email bataysk55@gmail.com YYYYYYYRRRRRRAAAAA")
    return None
