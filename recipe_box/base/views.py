from django.shortcuts import render, redirect
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.views.generic import TemplateView, ListView

#Importing stuff for sending reset password email
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

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
                        "uid":urlsafe_base64_encode(force_bytes(user.pk)),
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


