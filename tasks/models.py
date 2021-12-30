from django.db import models

# Create your models here.
class Task(models.Model):
    link = models.URLField()
    header = models.CharField(max_length=50)
    description = models.TextField(blank=True)


class Changes(models.Model):
    tasks_changes = models.JSONField()
