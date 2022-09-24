from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail 

class User(AbstractUser):
    email_confirmed = models.BooleanField(default = False)

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            "clown@kek.com",
            [self.email],
        )

class Task(models.Model):
    title = models.CharField(max_length=144)
    description = models.TextField(max_length=300)
    deadline = models.DateTimeField()
    task_type = models.CharField(max_length=66)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
