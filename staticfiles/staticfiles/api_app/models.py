from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyTask(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)


    # def __str__(self):
    #     return self.name




