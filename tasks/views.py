from urllib import request
from django.shortcuts import reverse
from django.views import generic

from .models import Task
from .forms import TaskForm

class TaskListView(generic.ListView): 
    template_name = "tasks/task_list.html"
    queryset = Task.objects.all()
    context_object_name = "tasks"

class TaskDetailView(generic.DetailView):
    template_name = "tasks/task_detail.html"
    queryset = Task.objects.all()
    context_object_name = "task"

class TaskCreateView(generic.CreateView):
    template_name = "tasks/task_create.html"
    form_class = TaskForm  

    def get_success_url(self):
        return reverse('tasks:task-detail', args = [ self.object.pk ]) 

class TaskUpdateView(generic.UpdateView):
    template_name = "tasks/task_update.html"
    queryset = Task.objects.all()
    form_class = TaskForm  

    def get_success_url(self):
        return reverse('tasks:task-detail', args = [ self.object.pk ]) 

class TaskDeleteView(generic.DeleteView):
    template_name = "tasks/task_delete.html"
    queryset = Task.objects.all()

    def get_success_url(self):
        return reverse('tasks:task-list') 