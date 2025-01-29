from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null = True)
    name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 100,db_index=True)

