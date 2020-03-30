from django.db import models
from django.utils import timezone

class Complain(models.Model):
    student_name = models.CharField(max_length=128, null=True, blank=True,)
    title = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title