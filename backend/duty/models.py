from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class VisitorTask(models.Model):
    sale_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    user         = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # tasks        = models.ManyToManyField(DefineTask, on_delete=models.CASCADE)
    task         = models.ManyToManyField()
    start_at     = models.DateField()
    end_at       = models.DateField()
    
    def __str__(self) -> str:
        return f"{self.user} {self.start_at} {self.end_at}"


class TaskDone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    compeleted_task = models.ForeignKey(VisitorTask, on_delete=models.CASCADE)
    task_done       = models.BooleanField()
    location        = models.Expression()
    
    def __str__(self) -> str:
        return f"{self.user} {self.compeleted_task}"
