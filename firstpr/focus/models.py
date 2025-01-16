from django.db import models

class Baners(models.Model):
    user = models.ForeignKey('start.Person', on_delete=models.CASCADE)
    name = models.CharField(max_length = 78)
    day = models.DateField()
    time = models.DateTimeField()
    color = models.CharField(max_length  = 7)
