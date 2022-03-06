from django.urls import path
# from .views import TaskList
from .import views



urlpatterns = [
    # path('', TaskList.as_view(), name='home'),zz
    path('', views.index, name='home'),
    path('tasks', views.Tasklist, name='tasks'),
    path('delete/<str:pk>', views.removData, name ='delete'),
    path('article_detail/<str:pk>', views.updateTask,name ='article_detail'),
    ]

     # path('', views.ShowTask.as_view(), name = 'list'),
    # path('update_task/<str:pk>', views.updateTask, name ='update_task'),