from django.urls import path

from tasks.views import (
    task_list, 
    task_retrieve,
    task_create,
    task_delete,
    task_update,
)

app_name='tasks'
urlpatterns = [
    path('', task_list, name='index'),
    path('task/<int:id>/', task_retrieve, name='detail'),
    path('task-create/', task_create, name='create'),
    path('task/<int:id>/delete', task_delete, name='delete'),
    path('task/<int:id>/edit', task_update, name='edit'),
]