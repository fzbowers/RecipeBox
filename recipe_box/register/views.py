from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView

from base.models import Recipes

# Create your views here.
def register(response):
    form = UserCreationForm()
    return render(response, "account.html", {"form":form})


class SearchResultsView(ListView):
    model = Recipes
    template_name = 'search.html'

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = Recipes.objects.filter(
            Q(title__icontains=query) | Q(section__icontains=query)
        )
        return object_list
