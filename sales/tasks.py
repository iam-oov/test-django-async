import time
import logging
from celery import shared_task

from mysite.celery import app
from .utils import get_redis

logger = logging.getLogger(__name__)


@app.task
def waitNSeconds(n):
    time.sleep(n)


@shared_task
def hello():
    print("Hello there!")


@shared_task
def increment_counter(choice_id):
    logger.info("increment {0}".format(choice_id))
    rconn = get_redis()
    rconn.incr("Choice%s" % choice_id)
    logger.info("done")
