from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Ingredient(models.Model):
    body = models.CharField(max_length = 100)
    
    class Meta:
        verbose_name = ('Ingredient')
        verbose_name_plural = ('Ingredients')

class Recipes(models.Model):
    title = models.CharField(max_length = 50)
    ingredients = models.ManyToManyField("Ingredient")

    class Meta:
        ordering = ['title']
        verbose_name = ('Recipe')
        verbose_name_plural = ('Recipies')

class Instruction(models.Model):

    text = models.TextField(blank=True, verbose_name=('Instrution'))
    recipe = models.ForeignKey(Recipes, related_name='instructions', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Instruction')
        verbose_name_plural = ('Instructions')
        ordering = ['order', 'id']

class Section(models.Model):
    name = models.CharField(max_length=120,
                            unique=True,
                            verbose_name=('Section'))
    order_index = models.PositiveIntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name = ('Section')
        verbose_name_plural = ('Sections')
        ordering = ['order_index']
