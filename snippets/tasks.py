from celery import shared_task
from time import sleep
from .models import Snippet


@shared_task
def reverse(text):
    print(text[::-1])

@shared_task
def create_user_and_notify(snippet_id):
    try:
        user_instance = Snippet.objects.get(pk=snipppet_id)
        print('successfully created')
        return snippet_id
    except Snippet.Doesnotexist:
        print('no id')
        return snippet_id
