from dataclasses import field, fields
from re import template
from django.shortcuts import render,redirect
from django.http.request import HttpRequest
from .models import *
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages,auth
from api_app import urls
from django.http import request
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django .urls import reverse_lazy

# from .forms import *

# Create your views here.

# def register(request):
#     if request.method =="POST":
        
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         username = request.POST['username']
#         password = request.POST['password']

#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exist')
#             return redirect('register')
#         else:
#             if User.objects.filter(email=email).exists():
#                 messages.error(request, 'Email already exist')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user( first_name=first_name, 
#                 last_name=last_name,email=email,
#                 username=username, password=password)

#                 user.save()
#                 messages.success(request, 'You are now registered')
#                 return redirect('login')
         
#     else:
#         return render(request,'register.html')




# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request,user)
#             messages.success(request, 'You are now logged in')
#             return redirect('tasks')
#         else:
#             messages.error(request, 'Invalid user')
#             return redirect('login')
#     else:
#         return render(request, 'accounts/login.html')



# Login class base view
class UserLogin(LoginView):
    template_name = 'accounts/login.html'
    fields =  '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')




# register function base view
def register(request):
    if request.method =="POST":
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exist')
            return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exist')
                return redirect('register')
            else:
                user = User.objects.create_user( first_name=first_name, 
                last_name=last_name,email=email,
                username=username, password=password)

                user.save()
                messages.success(request, 'You are now registered')
                return redirect('login')
         
    else:
        return render(request,'accounts/register.html')


# logout function base view
def logout(request):
    template_name = 'accounts/login.html'
    if request.method == "POST":
        auth.logout(request)
        messages.error(request, 'You are logged Out')
        return render(request, template_name)