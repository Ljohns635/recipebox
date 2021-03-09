# Generated by Django 3.1.6 on 2021-03-09 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=150)),
                ('author_bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RecipeItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('approx_time', models.CharField(max_length=20)),
                ('instructions', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_app.author')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='liked_recipe',
            field=models.ManyToManyField(blank=True, related_name='liked_recipe', to='recipe_app.RecipeItems'),
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
