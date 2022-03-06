from django import forms
from django.forms import ModelForm, fields

from .models import *

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = MyTask
        fields = '__all__'