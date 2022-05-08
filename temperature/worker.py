from __future__ import absolute_import

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery import shared_task

@periodic_task(run_every=(crontab(second='*/1')), name="some_task", ignore_result=True)
def some_task():
    print("SOME_TASK")

@shared_task
def task():
    print("TASK")