from django.shortcuts import render
from recipe_app.models import Author, RecipeItems

# Create your views here.
def index_view(request):
    recipes = RecipeItems.objects.all()
    return render(request, 'index.html', {'heading': 'Welcome to our RecipeBox', 'recipes': recipes})

def recipe_details(request, post_id):
    recipe = RecipeItems.objects.get(id=post_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def author_details(request, author_id):
    author_obj = Author.objects.get(id=author_id)
    recipes = RecipeItems.objects.filter(author=author_obj)
    return render(request, 'author_detail.html', {'author': author_obj, 'recipes': recipes})

