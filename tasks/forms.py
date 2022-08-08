from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as DefaultUserCreationForm

from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "deadline",
            "task_type",
            ]

class UserCreationForm(DefaultUserCreationForm):
    class Meta:
        model = get_user_model() 
        fields = ("username", "email")