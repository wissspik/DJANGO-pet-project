from django.db import models
from django.contrib.auth.models import User


class Url(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='text') # поменять related_name
    url = models.CharField(max_length= 71)

    def __str__(self):
        return self.url

class Text(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.ForeignKey(Url,on_delete=models.CASCADE,related_name='urls') # поменять related_name
    anonymity = models.BooleanField()
    text = models.CharField(max_length=3000)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    reaction = models.IntegerField()  # Например, 1 для лайка, 0 для дизлайка (если нужно)
    post = models.ForeignKey(Text, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Text, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)



    
