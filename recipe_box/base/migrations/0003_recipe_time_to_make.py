# Generated by Django 4.1.2 on 2022-11-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_alter_recipe_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="time_to_make",
            field=models.CharField(default=0, max_length=25),
        ),
    ]