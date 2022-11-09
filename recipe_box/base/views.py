from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, RecipeForm, IngredientForm, InstructionForm
from django.views.generic import TemplateView, ListView

#Importing stuff for sending reset password email
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
#from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.db.models import Q

from django.forms.models import modelformset_factory # querysets

from .models import Recipe, Ingredient, Instruction, Section

# Create your views here.


# search function based on tutorial from https://learndjango.com/tutorials/django-search-tutorial
class SearchResultsView(ListView):
    model = Recipe
    template_name = 'search.html'

    def get_queryset(self): 
        query = self.request.GET.get("q")
        object_list = Recipe.objects.filter(
            Q(name__icontains=query)  #| Q(description__icontains=query) made obsolete by change to model
        )
        return object_list


@login_required(login_url="/login")
def home(request):
    section_qs = Section.objects.filter(user=request.user)
    context = {
        "home_section_list": section_qs,
    }
    return render(request, "home.html", context)

@login_required
def search(request):
    return render(request, "search.html")

@login_required
def new_recipe(request):
    form = RecipeForm(request.POST or None)

    RecipeIngredientFormset = modelformset_factory(Ingredient, form=IngredientForm, extra=1)
    qs = Ingredient.objects.none()
    formset = RecipeIngredientFormset(request.POST or None, queryset=qs)
    
    context = {
        "form": form,
        "formset": formset
    }
    
    if form.is_valid() and formset.is_valid():
        print("IM IN CREATE IF")
        recipe = form.save(commit=False)
        recipe.user = request.user
        recipe.save()
        for form in formset:
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
        return redirect(recipe.get_absolute_url())

    return render(request, "new_recipe.html", context) 


#### NOT WORKING
@login_required
def edit_recipe(request, title=None, *args, **kwargs):
    obj = get_object_or_404(Recipe, name=title, user=request.user)
    context = {}

    form = RecipeForm(request.POST or None, instance=obj)

    RecipeIngredientFormset = modelformset_factory(Ingredient, form=IngredientForm, extra=0)
    qs = obj.ingredient_set.all() # []
    formset = RecipeIngredientFormset(request.POST or None, queryset=qs)
    context = {
        "form": form,
        "formset": formset,
        "object": obj
    }


        
    if all([form.is_valid(), formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        # formset.save()
        for form in formset:
            child = form.save(commit=False)
            child.recipe = parent
            child.save()
        context['message'] = 'Data saved.'
    else:
        print('This is form errors: ', form.errors)
        print('This is formset errors: ', formset.errors)
    if request.htmx:
        return render(request, "partials/forms.html", context)

    return render(request, "new_recipe.html", context) 


@login_required
def individual_recipe(request, title=None, *args, **kwargs):
    recipe_obj = None
    if title is not None:
        recipe_obj = get_object_or_404(Recipe, name=title, user=request.user)

    context = {
        "recipe_obj": recipe_obj
    }
    
    return render(request, "individual_recipe.html", context) 

@login_required
def individual_section(request, title=None):
    section_obj = None
    if title is not None:
        try:
            section_obj = Section.objects.get(name=title)
        except:
            section_obj = Nones
        if section_obj is None:
            return HttpResponse("Recipe Not found.")

    recipe_list = Recipe.objects.filter(Q(user=request.user) & Q(section=section_obj))
    
    context = {
        "section_obj": section_obj,
        "recipe_list": recipe_list,
    }
    return render(request, "individual_section.html", context) 

@login_required
def all_recipes(request):
    recipe_qs = Recipe.objects.filter(user=request.user)
    context = {
        "recipe_list": recipe_qs,
    }
    return render(request, "all_recipes.html", context) 

  
@login_required
def new_section(request):
    return render(request, "new_section.html")

@login_required
def account(request):
    return render(request, "account.html")



def create_account(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("login")
    else:
        form = RegisterForm()
    return render(response, "create_account.html", {"form": form})

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "registration/password_reset_email.txt"
                    c = {
                        "email":user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name':'Website',
                        "uid":urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="registration/password_reset.html", context={"password_reset_form":password_reset_form})


