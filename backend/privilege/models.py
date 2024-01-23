from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


User = settings.AUTH_USER_MODEL


class UserTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spent_time = models.DurationField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.pk} {self.user} {self.spent_time}"
    
    class Meta:
        ordering = ['-created_at']


class UserGivenScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    today_time =  models.DurationField(null=True, blank=True)
    user_score = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.user} {self.today_time} {self.user_score}"
    
    class Meta:
        ordering = ['user_score']
