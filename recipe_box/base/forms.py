from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, Instruction, Section, Food
from django.forms.widgets import CheckboxSelectMultiple


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["email"]

class SectionForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    name = forms.CharField(label="Name", label_suffix="", widget=forms.TextInput(attrs={'id' : "title"}))
    description = forms.CharField(label="Description", label_suffix="", required=False, widget=forms.Textarea(attrs={'placeholder' : "Enter description here...", 'id' : "freeform"}))
    class Meta:
        model = Section
        fields = ['name', 'description']
        ##fields = ['name', 'color', 'description']


class RecipeForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    name = forms.CharField(label="Title", label_suffix="", widget=forms.TextInput(attrs={'id' : "title"}))
    time_to_make = forms.CharField(label="Time", label_suffix="", widget=forms.TextInput(attrs={'id' : "time"}))
    time_unit = forms.BooleanField(label="Time_Unit", label_suffix="", widget=forms.TextInput(attrs={'id' : "time_unit"}))


    class Meta:
        model = Recipe
        fields = ['name', 'time_to_make', 'time_unit', 'section']

    # getting user sections
    def __init__(self, user, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['section'].label_suffix = ""
        self.fields['section'].widget = CheckboxSelectMultiple(attrs={'id' : "section-select"})
        self.fields['section'].queryset = Section.objects.filter(user=user)



class IngredientForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'id' : "ingredient", 'class' : "col-sm-6"}))
    quantity = forms.CharField(label='', widget=forms.TextInput(attrs={'id' : "amount", 'class' : "col-sm-2"}))
    unit = forms.CharField(label='', widget=forms.TextInput(attrs={'id' : "amount", 'class' : "col-sm-2"}))
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit']


class InstructionForm(forms.ModelForm):
    text = forms.CharField(label='', widget=forms.TextInput(attrs={'id' : "instruction", 'class' : "col-sm-10"}))
    class Meta:
        model = Instruction
        fields = ['text']

class ShoppingForm(forms.ModelForm):
    name = forms.CharField(label='Item', label_suffix="", widget=forms.TextInput(attrs={'id' : "shopping", 'class' : "col-sm-6"}))
    quantity = forms.CharField(label='Quantity', label_suffix="", widget=forms.TextInput(attrs={'id' : "shopping", 'class' : "col-sm-2"}))
    class Meta:
        model = Food
        fields = ['name', 'quantity']


