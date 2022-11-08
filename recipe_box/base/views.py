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
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from .models import Recipe, Ingredient, Instruction, Section

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
    section_qs = Section.objects.filter(user=request.user)
    context = {
        "section_list": section_qs,
    }
    
    print(request.POST)

    '''
    context = {
        "form": RecipeForm()
    }
   
    if request.method == "POST":
        title = request.POST.get("Title")
        time = request.POST.get("Time")
        section = request.POST.get("Section")
        print(title, time, section)

        recipe_obj = Recipe.objects.create(name=title,time_to_make=time,)
        
        context = {
            'recipe_obj': recipe_obj,
            'created': True
        }
        '''

    return render(request, "new_recipe.html", context)

'''
@login_required
def edit_recipe(request, title=None, *args, **kwargs):
    recipe_obj = get_object_or_404(Recipe, name=title, user=request.user)
    form = RecipeForm(request.POST or None, instance=recipe_obj)
    return render(request, "new_recipe.html", context)
'''


    #recipe_queryset = Ingredient.objects
    # check vid 18 to write ingredient - amount
    #recipe_queryset = Instruction.objects
@login_required
def individual_recipe(request, title=None, *args, **kwargs):
    recipe_obj = None
    if title is not None:
        try:
            recipe_obj = Recipe.objects.get(name=title)
        except:
            recipe_obj = None
        if recipe_obj is None:
            return HttpResponse("Recipe Not found.")

    context = {
        "name": recipe_obj.name,
        "time_to_make": recipe_obj.time_to_make,
        "description": recipe_obj.description
    }
    
    return render(request, "individual_recipe.html", context) 

@login_required
def all_recipes(request):
    recipe_qs = Recipe.objects.filter(user=request.user)
    #all() #qs = queryset
    context = {
        "recipe_list": recipe_qs,
    }
    return render(request, "all_recipes.html", context) 


#def new_recipe(request):
#    form = RecipeForm(request.POST or None)
#    if form.is_valid():
#        obj = form.save(commit=False)
#        obj.user = request.user
#        obj.save()
#    return render(request, "new_recipe.html", {"form": form})
  
@login_required
def new_section(request):
    return render(request, "new_section.html")

@login_required
def account(request):
    return render(request, "account.html")



#def individual_recipe(request, id=None):
#    obj = get_object_or_404(Recipe, id=id, user=request.user)
#    context = {
#        "object": obj
#    }
#return render(request, "individual_recipe.html", context)


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


