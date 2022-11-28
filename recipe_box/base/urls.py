from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    ## recipes ##
    path("", views.home, name="home"),
    path("search/",  views.search, name="search_results"),
    path("recipe/<str:title>/edit", views.edit_recipe, name="edit_recipe"),
    path("recipe/<str:title>/", views.individual_recipe, name="individual_recipe"),
    path("recipe/", views.new_recipe, name="new_recipe"),
    path("all_recipes/", views.all_recipes, name="all_recipes"),
    path("section/<str:title>/edit", views.edit_section, name="edit_section"),
    path("section/<str:title>/", views.individual_section, name="individual_section"),
    path("section/", views.new_section, name="new_section"),

     ## account ##
    path("account/", views.account, name="account"),
    path("create_account/", views.create_account, name="create_account"),
    path("change_password/", views.change_password, name='change_password'),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete.html'),
    
    ## shopping list ##
    path("shopping_list/", views.shopping_list, name="shopping_list"),
    path("add/", views.shopping_list_add),
    path("delete/<int:Food_id>/", views.shopping_list_delete)
]
