from django.conf import settings
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Section(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True,)
    description = models.TextField(null=True, blank=True)
    order_index = models.PositiveIntegerField(null=True, blank=True)
    color = models.CharField(max_length = 16, default="#ffffff")
    
    class Meta:
        verbose_name = ('Section')
        verbose_name_plural = ('Sections')
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    slug = models.SlugField(blank=True, null=True)
    ## description = models.TextField(null=True, blank=True) ## DON"T NEED
    time_to_make = models.CharField(max_length = 25, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    pinned = models.BooleanField(default=False)

    class Meta:
        verbose_name = ('Recipe')
        verbose_name_plural = ('Recipes')

    def get_ingredients_children(self):
        return self.ingredient_set.all()

    '''
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    '''

    def get_absolute_url(self):
        return reverse("individual_recipe", kwargs={"title": self.name})
        
    def get_edit_url(self):
        return reverse("edit_recipe", kwargs={"title": self.name})


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    quantity = models.CharField(max_length = 50)
    unit = models.CharField(max_length = 50)
    class Meta:
        verbose_name = ('Ingredient')
        verbose_name_plural = ('Ingredients')
    
    '''
    def __str__(self):
        return self.name
    '''

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()

class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    class Meta:
        verbose_name = ('Instruction')
        verbose_name_plural = ('Instructions')