from celery import shared_task
from datetime import time
from django.utils.timezone import get_current_timezone

from .models import UserTime, ScoreComputation, UserGivenScore

from django.conf import settings


User = settings.AUTH_USER_MODEL


@shared_task
def caculate_whole_time():
    if get_current_timezone() == time(hour=23, minute=0, second=0):
        k = 0
        for user in User.objects.all():
            pass
