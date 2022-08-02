from django.urls import path

from tasks.views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

app_name='tasks'
urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>/edit', TaskUpdateView.as_view(), name='task-update'),
]