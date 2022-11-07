from django.conf import settings
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Section(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True,)
    description = models.TextField(null=True, blank=True)
    order_index = models.PositiveIntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name = ('Section')
        verbose_name_plural = ('Sections')

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    description = models.TextField(null=True, blank=True)
    time_to_make = models.CharField(max_length = 25, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    pinned = models.BooleanField(default=False)

    class Meta:
        verbose_name = ('Recipe')
        verbose_name_plural = ('Recipes')

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    quantity = models.CharField(max_length = 50)
    unit = models.CharField(max_length = 50)
    class Meta:
        verbose_name = ('Ingredient')
        verbose_name_plural = ('Ingredients')


class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    class Meta:
        verbose_name = ('Instruction')
        verbose_name_plural = ('Instructions')