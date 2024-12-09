from django.db import models
from django.utils import timezone

class Model_ToDoWeb(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(max_length=300)
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"TITLE: {self.title} DETAIL: {self.detail} DATE: {self.date}"