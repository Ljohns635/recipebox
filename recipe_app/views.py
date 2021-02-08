from django.shortcuts import render, HttpResponseRedirect, reverse
from recipe_app.models import Author, RecipeItems
from recipe_app.forms import AddAuthorForm, AddRecipeForm

# Create your views here.
def index_view(request):
    recipes = RecipeItems.objects.all()
    return render(request, 'index.html', {'heading': 'Welcome to RecipeBox', 'recipes': recipes})

def recipe_details(request, post_id):
    recipe = RecipeItems.objects.get(id=post_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def author_details(request, author_id):
    author_obj = Author.objects.get(id=author_id)
    recipes = RecipeItems.objects.filter(author=author_obj)
    return render(request, 'author_detail.html', {'author': author_obj, 'recipes': recipes})

def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    
    form = AddAuthorForm()
    return render(request, 'generic_forms.html', {'form':form})

def add_recipe(request):
    context = {}
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_item = RecipeItems.objects.create(
                title = data['title'],
                author = data['author'],
                approx_time = data['approx_time'],
                instructions = data['instructions']
            )

            return HttpResponseRedirect(reverse('recipe_details', args=[new_item.id]))
    
    form = AddRecipeForm()
    context.update({'form':form})
    return render(request, 'generic_forms.html', context)