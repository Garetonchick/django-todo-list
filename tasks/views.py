from urllib import request
from django.shortcuts import reverse
from django.views import generic
from django.contrib.auth import mixins as auth_mixins

from .models import Task
from .forms import TaskForm

class LandingPageView(generic.TemplateView):
    template_name = "landing_page.html"

class TaskListView(auth_mixins.LoginRequiredMixin, generic.ListView): 
    template_name = "tasks/task_list.html"
    queryset = Task.objects.all()
    context_object_name = "tasks"

class TaskDetailView(auth_mixins.LoginRequiredMixin, generic.DetailView):
    template_name = "tasks/task_detail.html"
    queryset = Task.objects.all()
    context_object_name = "task"

class TaskCreateView(auth_mixins.LoginRequiredMixin, generic.CreateView):
    template_name = "tasks/task_create.html"
    form_class = TaskForm  

    def get_success_url(self):
        return reverse('tasks:task-detail', args = [ self.object.pk ]) 

class TaskUpdateView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = "tasks/task_update.html"
    queryset = Task.objects.all()
    form_class = TaskForm  

    def get_success_url(self):
        return reverse('tasks:task-detail', args = [ self.object.pk ]) 

class TaskDeleteView(auth_mixins.LoginRequiredMixin, generic.DeleteView):
    template_name = "tasks/task_delete.html"
    queryset = Task.objects.all()

    def get_success_url(self):
        return reverse('tasks:task-list') 