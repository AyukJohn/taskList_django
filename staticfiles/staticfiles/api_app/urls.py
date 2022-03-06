from django.urls import path
from .import views


urlpatterns = [
      path('', views.index,),

    # path('', views.ShowTask.as_view(), name = 'list'),
    # path('update_task/<str:pk>', views.updateTask, name ='update_task'),
    path('delete/<str:pk>', views.removData, name ='delete'),
    path('article_detail/<str:pk>', views.updateTask,name ='article_detail'),
    ]