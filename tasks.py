from mysite.celery import app
import time


@app.task
def waitNSeconds(n):
    time.sleep(n)
