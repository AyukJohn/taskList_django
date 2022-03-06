from django.urls import path
from .import views
# from .views import *



urlpatterns = [
      # path('', views.login, name='login'),
      path('', views.UserLogin.as_view(), name='login'),
      path('register', views.register, name='register'),
      path('logout', views.logout, name='logout'),
    ]