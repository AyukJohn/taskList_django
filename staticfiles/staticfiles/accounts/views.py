from django.shortcuts import render,redirect
from django.http.request import HttpRequest
from .models import *
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages

# from .forms import *

# Create your views here.

def register(request):
    if request.method =="POST":
        messages.error(request, 'just testing')
        return redirect('register')
        # first_name = request.POST['first_name'],
        # last_name = request.POST['last_name'],
        # email = request.POST['email'],
        # username = request.POST['username'],
        # password = request.POST['password'],
    else:
        return render(request,'register.html')




def login(request):
    return render(request, 'login.html')