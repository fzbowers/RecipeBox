# Sprint n (1, 2, 3 or 4)

Katrina Marks, KatrinaMarks, Recipe Box

### What you planned to do
* [Issue #7](https://github.com/utk-cs340-fall22/RecipeBox/issues/7) : create code for the input to create an account
* [Issue #8](https://github.com/utk-cs340-fall22/RecipeBox/issues/8) : figure out how to store users
* [Issue #9](https://github.com/utk-cs340-fall22/RecipeBox/issues/9) : create code for the input to login to an existing account

### What you did not do
* Django will automatically store the users once the admin page is set up, but I have not set up the admin page yet.

### What problems you encountered
* I had to get used to using Visual Studio Code instead of vim, because I did not want to try coding for a website in vim.
* Reading all the code I didn't write to understand the organization of our website was confusing at first.
* When I tried making a separate app for creating an account, the code did not work, so for now that code is in the base app.

### Issues you worked on
* [#7](https://github.com/utk-cs340-fall22/RecipeBox/issues/7) : create code for the input to create an account
* [#9](https://github.com/utk-cs340-fall22/RecipeBox/issues/9) : create code for the input to login to an existing account

### Files you worked on
* RecipeBox/recipe_box/recipe_box/settings.py
* RecipeBox/recipe_box/recipe_box/urls.py
* RecipeBox/recipe_box/base/urls.py
* RecipeBox/recipe_box/base/views.py
* RecipeBox/recipe_box/base/forms.py
* RecipeBox/recipe_box/templates/account.html
* RecipeBox/recipe_box/templates/create_account.html
* RecipeBox/recipe_box/templates/registration/login.html 

### What you accomplished
* I created a functioning create account page. Django did a lot of the work for me. I used Django's base create account form.
Then I made it look nicer using crispy forms and bootstrap. I also added an email field 
(Give a description of the features you added or tasks you accomplished. Provide some detail here. This section will be a little longer than the bulleted lists above) 
