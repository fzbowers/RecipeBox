from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, Instruction, Section


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["email", "password"]

class SectionForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    name = forms.CharField(label="Name",label_suffix="", widget=forms.TextInput(attrs={'id' : "title"}))
    description = forms.CharField(label="Description", label_suffix="", widget=forms.Textarea(attrs={'placeholder' : "Enter description here...", 'id' : "freeform"}))
    #color = 
    class Meta:
        model = Section
        fields = ['name', 'description']
        ##fields = ['name', 'color', 'description']



class RecipeForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    #SECTION_CHOICES = [tuple([x,x]) for x in user_section_list range(1,32)]

    name = forms.CharField(label="Title", label_suffix="", widget=forms.TextInput(attrs={'id' : "title"}))
    time_to_make = forms.CharField(label="Time", label_suffix="", widget=forms.TextInput(attrs={'id' : "time"}))
    
    class Meta:
        model = Recipe
        fields = ['name', 'time_to_make']
   

class IngredientForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'id' : "ingredient", 'class' : "col-sm-6"}))
    quantity = forms.CharField(label='', widget=forms.TextInput(attrs={'id' : "amount", 'class' : "col-sm-2"}))
    unit = forms.CharField(label='', widget=forms.TextInput(attrs={'id' : "amount", 'class' : "col-sm-2"}))
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit']


class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['text']


