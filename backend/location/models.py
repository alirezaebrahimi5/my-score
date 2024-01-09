from django.db import models
from django.conf import settings
from django.db.models import F 
from django.core.validators import RegexValidator
from django_jalali.db import models as jmodels 


User = settings.AUTH_USER_MODEL


class UserLocation(models.Model):
    numbers    = RegexValidator(r'^[0-9a]*$', message='تنها اعداد پذیرفته میشوند')
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude   = models.CharField(validators=[numbers], max_length=20)
    longitude  = models.DecimalField(validators=[numbers], max_length=20)
    where_is   = models.GeneratedField(expression=F("latitude") + F("longitude"), output_field=models.CharField(), db_persist=True)
    create_at  = jmodels.jDateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user} {self.where_is}"
