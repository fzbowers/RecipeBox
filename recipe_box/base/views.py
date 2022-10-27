from django.shortcuts import render, redirect
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.views.generic import TemplateView, ListView

from .models import Recipe

# Create your views here.

# search function based on tutorial from https://learndjango.com/tutorials/django-search-tutorial
class SearchResultsView(ListView):
    model = Recipe
    template_name = 'search.html'

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = Recipe.objects.filter(
            Q(title__icontains=query) | Q(section__icontains=query)
        )
        return object_list

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

def login(request):
    return render(request, "registration/login.html")

def individual_recipe(request):
    return render(request, "individual_recipe.html")

def create_account(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("login")
    else:
        form = RegisterForm()
    return render(response, "create_account.html", {"form": form})
