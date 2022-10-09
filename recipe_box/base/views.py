from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def search(request):
    return render(request, "search.html")
  
def new_recipe(request):
    return render(request, "new_recipe.html")
  
def all_recipes(request):
    return render(request, "all_recipes.html")

def new_section(request):
    return render(request, "new_section.html")
  
def all_sections(request):
    return render(request, "all_sections.html")

def account(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        form = UserCreationForm()
    return render(response, "account.html", {"form": form})