from django.db import models
import uuid
# from django.contrib.auth.models import User  
from TODO_web_app.settings import AUTH_USER_MODEL as User
# from django.contrib.auth.models import AbstractUser
# Create your models here


    
class Task(models.Model):
    uuid =  models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default= False)
    priority = models.IntegerField(default=4)

    def __str__(self):
        return self.name

    