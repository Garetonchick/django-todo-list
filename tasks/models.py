from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=144)
    description = models.CharField(max_length=200)
    deadline = models.DateTimeField()
    task_type = models.CharField(max_length=66)

    def __str__(self):
        return self.title
