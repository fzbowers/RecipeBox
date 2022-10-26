from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView

from base.models import Recipe

# Create your views here.
def register(response):
    form = UserCreationForm()
    return render(response, "account.html", {"form":form})



