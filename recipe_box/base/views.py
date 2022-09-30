from django.shortcuts import render

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

def account(request):
    return render(request, "account.html")