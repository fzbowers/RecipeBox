from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Ingredient(models.Model):
    body = models.CharField(max_length = 100)
    
class Recipes(models.Model):
    title = models.CharField(max_length = 50)
    ingredients = models.ManyToManyField("Ingredient")
