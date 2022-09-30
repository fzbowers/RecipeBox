from django.urls import path
from . import views
  

# All pages of the website
urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("new_recipe/", views.new_recipe, name="new_recipe"),
    path("all_recipes/", views.all_recipes, name="all_recipes"),
    path("new_section/", views.new_section, name="new_section"),
    path("all_sections/", views.all_sections, name="all_sections"),
    path("account/", views.account, name="account"),
]