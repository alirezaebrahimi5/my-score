from celery import shared_task
from django.utils.timezone import get_current_timezone

from .models import UserTime, ScoreComputation, UserGivenScore


@shared_task
def caculate_whole_time():
    return 
