<<<<<<< HEAD
=======
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
    longitude  = models.CharField(validators=[numbers], max_length=20)
    # where_is   = models.GeneratedField(expression=F("latitude") + F("longitude"), output_field=models.CharField(), db_persist=True)
    created_at  = jmodels.jDateTimeField(auto_now_add=True)
    
    @property
    def where_is(self):
        return '(' + str(self.latitude) + ',' + str(self.longitude) + ')'
    
    def __str__(self) -> str:
        return f"{self.user} {self.where_is}"
    
    class Meta:
        ordering = ['user']
<<<<<<< HEAD
>>>>>>> f64a207 (adding some of location functionality)
=======


class NewLocation(models.Model):
    numbers = RegexValidator(r'^[0-9a]*$', message='تنها اعداد پذیرفته میشوند')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
<<<<<<< HEAD
>>>>>>> b7b9b89 (some features added)
=======
    title = models.CharField(max_length=144)
    lat = models.CharField(validators=[numbers], max_length=20)
    log = models.CharField(validators=[numbers], max_length=20)
    address = models.CharField(max_length=4096)
    
    def __str__(self) -> str:
        return f"{self.user} {self.title}"
>>>>>>> 50a5c07 ( adding new features into location app and add media path for images)
