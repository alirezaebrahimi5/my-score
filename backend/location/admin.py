<<<<<<< HEAD
=======
from django.contrib import admin

from .models import UserLocation


@admin.register(UserLocation)
class ULAdmin(admin.ModelAdmin):
    list_display = ['user', 'where_is']
    search_fields = ['user']
>>>>>>> f64a207 (adding some of location functionality)
