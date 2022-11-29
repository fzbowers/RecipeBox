from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Recipe, Section, Ingredient, Instruction, Food

User = get_user_model() 



## Display recipies in admin page  ##

class IngredientsInline(admin.StackedInline):
    model = Ingredient
    extra = 0

class RecipesAdmin(admin.ModelAdmin):
    inlines = [IngredientsInline]
    list_display = ['user', 'name', 'slug']
    raw_id_fields = ['user']

    def get_form(self, request, obj=None, **kwargs):
        form = super(RecipesAdmin, self).get_form(request, obj, **kwargs)
        return form 

class SectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    raw_id_fields = ['user']

admin.site.register(Recipe, RecipesAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Instruction)
admin.site.register(Food)
