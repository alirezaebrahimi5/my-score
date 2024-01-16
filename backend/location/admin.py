<<<<<<< HEAD
=======
from django.contrib import admin

from .models import UserLocation, NewLocation


@admin.register(UserLocation)
class ULAdmin(admin.ModelAdmin):
    list_display = ['user', 'where_is']
    search_fields = ['user']
<<<<<<< HEAD
>>>>>>> f64a207 (adding some of location functionality)
=======


@admin.register(NewLocation)
class NLAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']
    search_fields = ['user', 'title']
>>>>>>> 50a5c07 ( adding new features into location app and add media path for images)
