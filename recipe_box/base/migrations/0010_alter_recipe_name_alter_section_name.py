# Generated by Django 4.1.1 on 2022-11-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_section_name_section_unique name for each user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]