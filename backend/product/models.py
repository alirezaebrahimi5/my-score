<<<<<<< HEAD
=======
from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Product(models.Model):
    title = models.CharField()
    img = models.ImageField(upload_to='product/')
    slug = models.SlugField()
    price = models.DecimalField()
    description = models.CharField()
    capacity = models.OneToOneField()


class Product_by_S_M(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
>>>>>>> b7b9b89 (some features added)
