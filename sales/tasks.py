import time
from celery import shared_task

from mysite.celery import app


@app.task
def waitNSeconds(n):
    time.sleep(n)


@shared_task
def hello():
    print("Hello there!")
