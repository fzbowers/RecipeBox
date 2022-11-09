from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.

User = get_user_model() ## MIGHT NOT NEED

#display recipies in admin page 
from .models import Recipe, Section, Ingredient, Instruction

class IngredientsInline(admin.StackedInline):
    model = Ingredient
    extra = 0

class RecipesAdmin(admin.ModelAdmin):
    inlines = [IngredientsInline]
    list_display = ['user', 'name']
    ## , 'section']
    raw_id_fields = ['user']

class SectionAdmin(admin.ModelAdmin):
    list_display = ['name']
    raw_id_fields = ['user']
    
admin.site.register(Recipe, RecipesAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Instruction)

