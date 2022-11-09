from django.urls import path
from . import views
from .views import SearchResultsView

# All pages of the website
urlpatterns = [
    path("", views.home, name="home"),
    path("search/",  SearchResultsView.as_view(), name="search_results"),
    path("new_recipe/", views.new_recipe, name="new_recipe"),
    path("recipes/<str:title>/edit", views.edit_recipe, name="edit_recipe"),
    path("recipes/<str:title>/", views.individual_recipe, name="individual_recipe"),
    path("recipes/", views.all_recipes, name="all_recipes"),
    path("new_section/", views.new_section, name="new_section"),
    path("account/", views.account, name="account"),
    path("create_account/", views.create_account, name="create_account"),
    path("password_reset/", views.password_reset_request, name="password_reset")
]
