from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from recipe_app.models import Author, RecipeItems
from recipe_app.forms import AddAuthorForm, AddRecipeForm

# Create your views here.
def index_view(request):
    message = 'Jacob is here'
    recipes = RecipeItems.objects.all()
    return render(request, 'index.html', {'heading': 'Welcome to our RecipeBox', 'recipes': recipes, 'message':message})

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
                description= data['description'],
                approx_time = data['approx_time'],
                instructions = data['instructions']
            )

            return HttpResponseRedirect(reverse('recipe_details', args=[new_item.id]))
    
    form = AddRecipeForm()
    context.update({'form':form})
    return render(request, 'generic_forms.html', context)


@login_required
def edit_view(request, post_id):
    context = {}
    edit = RecipeItems.objects.get(id=post_id)
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            edit.title = data['title']
            edit.author = data['author']
            edit.approx_time = data['approx_time']
            edit.description = data['description']
            edit.instructions = data['instructions']
            edit.save()
            return HttpResponseRedirect(reverse(
                                        'recipe_detail',
                                        args=[edit.id]))

    form = AddRecipeForm(initial={
        'title': edit.title,
        'author': edit.author,
        'description': edit.description,
        'approx_time': edit.approx_time,
        'instructions': edit.instructions,
        })
    context.update({'form': form})
    return render(request, 'generic.html', context)