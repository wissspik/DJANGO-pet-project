from django.db import models

class Person(models.Model):
    name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20,db_index=True)

