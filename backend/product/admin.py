from django.contrib import admin

from .models import Product, Product_by_S_M


@admin.register(Product)
class PAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'capacity']
    prepopulated_fields = {
        'slug': ('title',),
    }


@admin.register(Product_by_S_M)
class PSMAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
