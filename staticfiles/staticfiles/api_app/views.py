from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views import View


# Create your views here.

# class ShowTask(View):

#     # myForms = TaskForm()
#     template_name = 'index.html'
    

#     def get(self,request):
#         tasks = MyTask.objects.all()
#         holder = {'tasks':tasks}
#         return render(request, self.template_name,holder)

    
#     def post(self, request):
#         Forms = TaskForm(request.POST)
#         if Forms.is_valid():
#             Forms.save()
#             return redirect('/')


# class SingleTask(View):
#     myForms = TaskForm()


#     def get_data(self,pk):
#         try:
#             return MyTask.objects.get(id = pk)

#         except MyTask.DoesNotExist:
#             return HttpResponseNotFound('Item not found')

#     def put(self,request,pk):

#         tasks = self.get_data(pk)
        
#         form = self.myForms(request.POST, instance=tasks)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
        
        # context = {'form':form}
        # return render(request, 'tasks/update_task.html',context)



def index(request):
    # return HttpResponse('helo people')
    tasks = MyTask.objects.all()

    myForms = TaskForm()

    if request.method =="POST":
        myForms = TaskForm(request.POST)
        if myForms.is_valid():
            myForms.save()
        return redirect('/')

    holder = {'tasks':tasks}
    return render(request, 'index.html',holder)



def updateTask(request, pk):
    tasks = MyTask.objects.get(id=pk)

    form = TaskForm(instance=tasks)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')

    holder = {'tasks':tasks}
    return render(request, 'index.html')       





def removData(request,pk):
    tasks = MyTask.objects.get(id=pk)

    if request.method == "POST":
        tasks.delete()
        return redirect('/')
    
    holder = {'tasks':tasks}
    return render(request, 'index.html',holder)




