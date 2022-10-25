from django.contrib import admin

# Register your models here.

from .models import Recipes

class RecipesAdmin(admin.ModelAdmin):
    list_display = ("title", "section",)

admin.site.register(Recipes, RecipesAdmin)