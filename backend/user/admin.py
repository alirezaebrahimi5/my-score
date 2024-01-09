from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_jalali.admin.filters import JDateFieldListFilter

from .models import User, Profile


@admin.register(User)
class Admin(UserAdmin):
    list_display = ('identificationCode', 'first_name', 'last_name', 'mobile', 'role')
    filter_horizontal = ()
    list_filter = (
        ('joined_at', JDateFieldListFilter), 'is_active', 'role'
    )
    fieldsets = ()
    search_fields = ('identificationCode', 'first_name', 'last_name', 'mobile')
    ordering = ('joined_at', 'role')
