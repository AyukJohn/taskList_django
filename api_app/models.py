import django
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class MyTask(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, null=True,on_delete= models.CASCADE, blank=True)
    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['complete']



# user = models.ForeignKey(User, on_delete= models.CASCADE)
