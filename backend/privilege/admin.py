from django.contrib import admin

from .models import UserTime, UserGivenScore


@admin.register(UserTime)
class UTAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'spent_time']
    search_fields = ['user']


@admin.register(UserGivenScore)
class UGSAdmin(admin.ModelAdmin):
    list_display = ['user', 'today_time', 'user_score']
    list_filter = ['user_score']
    search_fields = ['user']
