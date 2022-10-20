from django.shortcuts import render, redirect
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

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

def account(request):
    return render(request, "account.html")

def landing(request):
    return render(request, "landing.html")

def individual_recipe(request):
    return render(request, "individual_recipe.html")

def create_account(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("account")
    else:
        form = RegisterForm()
    return render(response, "create_account.html", {"form": form})

def pagelogout(request):
    if request.method =="POST":
        pagelogout(request)
        return redirect('landing')