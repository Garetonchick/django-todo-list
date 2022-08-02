from urllib import request
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.views import generic

from .models import Task
from .forms import TaskForm

class TaskListView(generic.ListView): 
    template_name = "task_list.html"
    queryset = Task.objects.all()
    context_object_name = "tasks"

class TaskDetailView(generic.DetailView):
    template_name = "task_detail.html"
    queryset = Task.objects.all()
    context_object_name = "task"

class TaskCreateView(generic.CreateView):
    template_name = "task_create.html"
    form_class = TaskForm  

    def get_success_url(self):
        return reverse('tasks:detail', args = [ self.object.pk ]) 

class TaskUpdateView(generic.UpdateView):
    template_name = "task_update.html"
    queryset = Task.objects.all()
    form_class = TaskForm  

    def get_success_url(self):
        return reverse('tasks:detail', args = [ self.object.pk ]) 

class TaskDeleteView(generic.DeleteView):
    template_name = "task_delete.html"
    queryset = Task.objects.all()

    def get_success_url(self):
        return reverse('tasks:index') 