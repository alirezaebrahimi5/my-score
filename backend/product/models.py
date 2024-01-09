from django.db import models


class Duty:
    PRODUCT = 1
    SERVICE = 2
    
    DUTY = (
        (PRODUCT, 'محصولات'),
        (SERVICE, 'خدمات'),
    )


class Product(models.Model):
    tag   = models.PositiveSmallIntegerField(choices=Duty.DUTY, default=1)
    title = models.CharField(max_length=144)
