from django.urls import path 

from .views import *


urlpatterns = [
    path('new-location/', AddNewLocationAPIView.as_view(), name='new-location'),
]
