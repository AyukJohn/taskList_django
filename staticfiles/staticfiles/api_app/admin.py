from django.contrib import admin
from .models import *

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','complete', 'created')

admin.site.register(MyTask,TaskAdmin)