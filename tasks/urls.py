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
    path('', TaskListView.as_view(), name='index'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('task-create/', TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='delete'),
    path('task/<int:pk>/edit', TaskUpdateView.as_view(), name='edit'),
]