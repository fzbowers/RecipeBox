# Sprint 2

Katrina Marks, KatrinaMarks, Recipe Box

### What you planned to do
* [Issue #8](https://github.com/utk-cs340-fall22/RecipeBox/issues/8) : figure out how to store users
* [Issue #14](https://github.com/utk-cs340-fall22/RecipeBox/issues/14) : Create admin page
* [Issue #15](https://github.com/utk-cs340-fall22/RecipeBox/issues/15) : Research user access
* [Issue #16](https://github.com/utk-cs340-fall22/RecipeBox/issues/16) : Write code for logging out
* [Issue #17](https://github.com/utk-cs340-fall22/RecipeBox/issues/17) : Alter create account and login for landing page
* [Issue #29](https://github.com/utk-cs340-fall22/RecipeBox/issues/29) : Allow user to reset password


### What you did not do
* I didn't actually create an admin page, since it already exist, but I made an admin account so that we can access the admin page.
* I didn't actually do anything to store the users, since django handles it for us, but we can now see the users on the admin page.
* I started researching user access, but I have not wrote any code involving user access yet.
* Fatima did most of the stuff for the landing page, but I changed a few links. 
* I did not fully complete issue 29.

### What problems you encountered
* While all the html templates for resetting a password work, I have not been able to get the other code to work.
* When a user submits a valid email on the password reset page, they are supposed to be redirected to the password reset done page.
* I have not been able to figure out why this is not working; I've looked at multiple different tutorials, but will move this issue to sprint 3. 

### Issues you worked on
* [#8](https://github.com/utk-cs340-fall22/RecipeBox/issues/8) : figure out how to store users
* [#14](https://github.com/utk-cs340-fall22/RecipeBox/issues/14) : Create admin page
* [#15](https://github.com/utk-cs340-fall22/RecipeBox/issues/15) : Research user access
* [#16](https://github.com/utk-cs340-fall22/RecipeBox/issues/16) : Write code for logging out
* [#17](https://github.com/utk-cs340-fall22/RecipeBox/issues/17) : Alter create account and login for landing page
* [#29](https://github.com/utk-cs340-fall22/RecipeBox/issues/29) : Allow user to reset password

### Files you worked on
* RecipeBox/recipe_box/recipe_box/settings.py
* RecipeBox/recipe_box/recipe_box/urls.py
* RecipeBox/recipe_box/base/urls.py
* RecipeBox/recipe_box/base/views.py
* RecipeBox/recipe_box/templates/registration/password_reset.html
* RecipeBox/recipe_box/templates/account.html
* RecipeBox/recipe_box/templates/registration/password_reset_email.txt
* RecipeBox/recipe_box/templates/registration/password_reset_done.html
* RecipeBox/recipe_box/templates/registration/password_reset_confirm.html
* RecipeBox/recipe_box/templates/registration/password_reset_complete.html


### What you accomplished
* I learned how to make admin accounts so that we can see all of the users and their information.
* The user now has a logout option on the account page.
* I made decent progress on letting a user reset their password if they forgot it.    