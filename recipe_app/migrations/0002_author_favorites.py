# Generated by Django 3.1.6 on 2021-03-24 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='fav_recipes', to='recipe_app.RecipeItems'),
        ),
    ]
