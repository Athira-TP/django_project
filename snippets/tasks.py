from celery import shared_task
from time import sleep



@shared_task
def reverse(text):
    print(text[::-1])