from urllib import request
from django.shortcuts import redirect, render

from .models import Task
from .forms import TaskForm

def task_list(request):
    context = {
        'tasks': Task.objects.all()
    }

    return render(request, 'task_list.html', context)

def task_retrieve(request, id):
    context = {
        'task': Task.objects.get(id=id)
    }

    return render(request, 'task_retrieve.html', context)

def task_create(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }

    return render(request, "task_create.html", context)

def task_update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }

    return render(request, "task_update.html", context)

def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    return redirect("/") 