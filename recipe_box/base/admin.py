from django.contrib import admin

# Register your models here.

from .models import Recipe

class RecipesAdmin(admin.ModelAdmin):
    list_display = ("name", "section",)

admin.site.register(Recipe, RecipesAdmin)