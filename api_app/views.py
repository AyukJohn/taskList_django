from django.contrib import auth
from django.views.generic.list import ListView
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import MyTask
from .forms import *
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from functools import wrapsz
# from django.contrib.auth.models import User


# class TaskList(ListView):
#     model = MyTask


# @login_required




def index(request):
    return render(request, 'index.html')



@login_required
def Tasklist(request):
    
    # user = request.user
    # tasks = MyTask.objects.all()
    # if request.user.is_authenticated():
    tasks = MyTask.objects.filter(user=request.user)
    count = MyTask.objects.filter(complete=False).count()
    # tasks['count'] = tasks['tasks'].filter(complete=False).count()

    

    # myForms = TaskForm()

    if request.method =="POST":
        myForms = TaskForm(request.POST)
        if myForms.is_valid():
         data = myForms.save(commit=False)
         data.user = request.user
         data.save()

        return redirect('tasks')

    holder = {'tasks':tasks, 'count':count}

    return render(request, 'task.html',holder)




@login_required
def updateTask(request, pk):
    tasks = MyTask.objects.get(id=pk)

    form = TaskForm(instance=tasks)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
           data= form.save()
           data.user = request.user
           data.save()
        return redirect('tasks')

    holder = {'tasks':tasks}
    return render(request, 'index.html')       





@login_required
def removData(request,pk):
    tasks = MyTask.objects.get(id=pk)

    if request.method == "POST":
        tasks.delete()
        return redirect('tasks')
    
    holder = {'tasks':tasks}
    return render(request, 'index.html',holder)




