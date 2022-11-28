from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserChangeForm
from .forms import RegisterForm, EditProfileForm, RecipeForm, IngredientForm, InstructionForm, SectionForm, ShoppingForm
from django.views.generic import TemplateView, ListView
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory

from .models import Recipe, Ingredient, Instruction, Section, Food



## Recipe Views ##

#search page
#seach based on tutorial from https://linuxhint.com/build-a-basic-search-for-a-django/
@login_required
def search(request):
    recipe_list = []
    if request.method == "GET":
        query = request.GET.get('search')
        recipe_list = Recipe.objects.filter(
            Q(name__icontains=query) & Q(user=request.user) 
        )

        temp_ingredient_list = []

        temp_ingredient_list = Ingredient.objects.filter(
            Q(name__icontains=query)
        )

        ingredient_list = []

        for ingredient in temp_ingredient_list: 
            ingredient_list.append(ingredient.recipe)
            #print(temp_recipe)
            #if temp_recipe.user == request.user:
            #    ingredient_list.append(ingredient.recipe)
               

    context = {
    "recipe_list": recipe_list,
    "ingredient_list": ingredient_list,
    "query": query,
    }

    return render(request, "search.html", context)


#home page
@login_required(login_url="/login")
def home(request):
    section_qs = Section.objects.filter(user=request.user)
    pinned_qs = Recipe.objects.filter(Q(user=request.user) & Q(pinned=True))

    context = {
        "home_section_list": section_qs,
        "pinned_recipes_list": pinned_qs,
    }
    return render(request, "home.html", context)


#create new recipe page
@login_required
def new_recipe(request):
    user = request.user
    form = RecipeForm(user)
    IngredientFormset = inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=1)
    formset = IngredientFormset()
    InstructionFormset = inlineformset_factory(Recipe, Instruction, form=InstructionForm, extra=1)
    formset2 = InstructionFormset()

    if request.method == 'POST':
        form = RecipeForm(user, request.POST)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user # not sure if needed
            recipe.save()
            form.save_m2m()

            formset = IngredientFormset(request.POST or None, instance=recipe)
            if formset.is_valid():
                formset.save()

            formset2 = InstructionFormset(request.POST or None, instance=recipe)
            if formset2.is_valid():
                formset2.save()
                return redirect(recipe.get_absolute_url())
    
    context = {
        'form': form,
        'formset': formset,
        'formset2': formset2,
    }
    return render(request, "new_recipe.html", context) 


#edit recipe page
@login_required
def edit_recipe(request, title=None, *args, **kwargs):
    user = request.user
    recipe_obj = Recipe.objects.get(slug=title)

    form = RecipeForm(user, instance=recipe_obj)
    IngredientFormset = inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=0)
    formset = IngredientFormset(instance=recipe_obj)
    InstructionFormset = inlineformset_factory(Recipe, Instruction, form=InstructionForm, extra=0)
    formset2 = InstructionFormset(instance=recipe_obj)

    if request.method == 'POST':
        form = RecipeForm(user, request.POST, instance=recipe_obj)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user # not sure if needed
            recipe.save()
            form.save_m2m()
            
            formset = IngredientFormset(request.POST or None, instance=recipe)
            if formset.is_valid():
                formset.save()

            formset2 = InstructionFormset(request.POST or None, instance=recipe)
            if formset2.is_valid():
                formset2.save()
            return redirect(recipe.get_absolute_url())

    context = {
        'form': form,
        'formset': formset,
        'formset2': formset2,
    }
    return render(request, "new_recipe.html", context) 


#view recipe page
@login_required
def individual_recipe(request, title=None, *args, **kwargs):
    recipe_obj = None
    if title is not None:
        recipe_obj = get_object_or_404(Recipe, slug=title, user=request.user)

        if recipe_obj.pinned == True:
            is_pinned = True
        else:
            is_pinned = ''

        #pin and unpin recipe
        if "pinnedbtn" in request.POST:
            recipe_obj.pinned = True
            recipe_obj.save(update_fields=["pinned"])
            is_pinned = True
        if "unpinnedbtn" in request.POST:
            recipe_obj.pinned = False
            recipe_obj.save(update_fields=["pinned"])
            is_pinned = ''

        if "delete" in request.POST:
            recipe_obj.delete()
            return redirect("../../all_recipes")

    context = {
        "recipe_obj": recipe_obj,
        "is_pinned" : is_pinned
    }
    
    return render(request, "individual_recipe.html", context) 


#view individual section page 
@login_required
def individual_section(request, title=None, *args, **kwargs):
    section_obj = None
    if title is not None:
        section_obj = get_object_or_404(Section, slug=title, user=request.user)

        if "delete" in request.POST:
            section_obj.delete()
            return redirect("../../")

        description = ""
        description = section_obj.description

        print(title)
        recipe_list = Recipe.objects.filter(section__slug=title)

    context = {
        "section_obj": section_obj,
        "recipe_list": recipe_list,
        "description": description
    }

    return render(request, "individual_section.html", context) 


#veiw all recipes page
@login_required
def all_recipes(request):
    recipe_qs = Recipe.objects.filter(user=request.user)
    context = {
        "recipe_list": recipe_qs,
    }
    return render(request, "all_recipes.html", context) 


#create new section
@login_required
def new_section(request):
    form = SectionForm(request.POST or None)
    
    context = {
        "form": form,
    }

    if form.is_valid():
        section = form.save(commit=False)
        section.user = request.user
        section.save()     
        return redirect("../")

    return render(request, "new_section.html", context)


#edit section page
@login_required
def edit_section(request, title=None, *args, **kwargs):
    section_obj = Section.objects.get(slug=title)
    form = SectionForm(request.POST or None, instance=section_obj)

    if request.method == 'POST':
        if form.is_valid():
            section = form.save(commit=False)
            section.user = request.user
            section.save()
            return redirect(section.get_absolute_url())   

    context = {
        "form": form,
    }

    return render(request, "new_section.html", context)



## Shopping list views ##

#shopping list page
@login_required
def shopping_list(request):
    food_qs = Food.objects.filter(user=request.user)
    form = ShoppingForm(request.POST)
    context = {
        "food_list": food_qs,
        "ShoppingForm": ShoppingForm
    }
    return render(request, "shopping_list.html", context)


#add to list
@login_required
def shopping_list_add(request):
    #FoodToBuy_obj = None
    #FoodToBuy_obj = get_object_or_404(FoodToBuy, user=request.user)
    #return render(request, "shopping_list.html", {"FoodToBuy": FoodToBuy.objects.all()})
    form = ShoppingForm(request.POST)

    context = {
       "ShoppingForm": ShoppingForm
    }

    if form.is_valid():
        food = form.save(commit=False)
        food.user = request.user
        food.save()
        return HttpResponseRedirect('/shopping_list/')

  #context = {
     #   "shopping_list": FoodToBuy
    #}
    #if Food != None:
       # return render(request, "shopping_list.html", context, {"Food": Food.objects.filter(user=request.user)})
    return render(request, "shopping_list.html", context)


#remove from list
@login_required
def shopping_list_delete(request, Food_id):
    Food.objects.get(id=Food_id).delete()
    return HttpResponseRedirect('/shopping_list/')



## Acccount related views ##

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
                    return redirect ("/password-reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="registration/password_reset.html", context={"password_reset_form":password_reset_form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password successfully updated :)')
            return redirect('account')
        else:
            messages.error(request, 'Error :(')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

def edit_profile(request):
   if request.method == "POST":
      form = EditProfileForm(request.POST, instance=request.user)
      if form.is_valid():
        form.save()
        return redirect('account')
   else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)
