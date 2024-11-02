# from django.db import models

# class Recipe(models.Model):
#     title = models.CharField(max_length=100)
#     ingredients = models.TextField()
#     instructions = models.TextField()

#     def __str__(self):
#         return self.title

from django.contrib.postgres.fields import ArrayField
from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    password = models.CharField(max_length=30)
    favorites = ArrayField(models.CharField(max_length=100), blank=True, default=list)  
