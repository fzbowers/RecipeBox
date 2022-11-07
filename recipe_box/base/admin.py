from django.contrib import admin

# Register your models here.

#display recipies in admin page 
from .models import Recipe, Section, Ingredient, Instruction

class RecipesAdmin(admin.ModelAdmin):
    list_display = ("name", "section",)

class SectionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    
admin.site.register(Recipe, RecipesAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Ingredient)
admin.site.register(Instruction)

