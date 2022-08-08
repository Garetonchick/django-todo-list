from urllib import request
from django.shortcuts import reverse, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import mixins as auth_mixins
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib import messages

from .models import Task, User
from .forms import TaskForm, UserCreationForm
from .tokens import account_activation_token_generator

class LandingPageView(generic.TemplateView):
    template_name = "landing_page.html"

class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        print(f"New user pk is: {user.pk}")
        subject = "Activate your account"
        message = render_to_string("registration/activation_email.html", {
            'user': user,
            'domain': "127.0.0.1:8000",
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token_generator.make_token(user),
        }) 

        user.email_user(subject, message)

        return super().form_valid(form)

class EmailConfirmedView(generic.View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid) 
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None 

        print(f"Username of confirmed user is: {user.username}")

        if user is not None and account_activation_token_generator.check_token(user, token): 
            user.email_confirmed = True
            user.save()
            messages.success(request, "Your account has been confirmed")
            return redirect(reverse('login'))
        else:
            messages.warning(request, "The confirmation link was invalid, possibly because it has already been used.")  
            return redirect(reverse('landing-page'))
         

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