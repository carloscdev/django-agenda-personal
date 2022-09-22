from django.db import models
from datetime import date

class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    estimated_end = models.DateField(default=date.today)
    priority = models.IntegerField(default=3)
    finished = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
