from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, Instruction, Section

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        #fields = ['name', 'description']
        fields = ['name', 'color', 'description']

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'time_to_make']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit']

class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['text']
