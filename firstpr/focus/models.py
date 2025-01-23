from django.db import models
from start.models import Person

class URL(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='posts')  # Связаю по
    url = models.CharField(max_length = 71)
    url_Text = models.CharField(max_length=300,null = True,blank = True)
    url_title = models.CharField(max_length = 100,null = True,blank = True)
    url_subtitle = models.CharField(max_length = 100,null = True,blank = True)


