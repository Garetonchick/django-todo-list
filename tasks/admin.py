from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Task

# Register your models here.

admin.site.register(Task)
admin.site.register(get_user_model())
