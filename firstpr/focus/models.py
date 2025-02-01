from django.db import models
from django.contrib.auth.models import User


class Url(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='text')
    url = models.CharField(max_length= 71)

class Text(models.Model):
    id = models.AutoField(primary_key=True)
    url_id = models.ForeignKey(Url,on_delete=models.CASCADE,related_name='urls')
    anonymity = models.BooleanField()
    text = models.CharField(max_length=3000)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)

class Likes(models.Model):
    id = models.AutoField(primary_key=True)
    reaction = models.IntegerField()
    url_id = models.ForeignKey(Text,on_delete=models.CASCADE,related_name='urls')
    user_id = models.CharField(max_length=50)



    
