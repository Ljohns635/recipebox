from django.shortcuts import render, HttpResponseRedirect, reverse
from recipe_app.models import Author, RecipeItems
from recipe_app.forms import AddAuthorForm, AddRecipeForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test

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


@login_required
@user_passes_test(lambda user: user.is_staff, login_url ='homepage')
def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
        
        #if request.user.is_staff:
    form = AddAuthorForm()
    return render(request, 'generic_forms.html', {'form':form})


@login_required
def add_recipe(request):
    context = {}
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_item = RecipeItems.objects.create(
                title = data['title'],
                author = request.user.author,
                description = data['description'],
                approx_time = data['approx_time'],
                instructions = data['instructions']
            )

            return HttpResponseRedirect(reverse('recipe_details', args=[new_item.id]))
    
    form = AddRecipeForm()
    context.update({'form':form})
    return render(request, 'generic_forms.html', context)


# def signup_view(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_user = User.objects.create_user(
#                 username=data['username'], password=data['password']
#             )
#             Author.objects.create(
#                 author_name=data['author_name'], author_bio=data['author_bio'], user=new_user
#             )
#             return HttpResponseRedirect(reverse('homepage'))    


#     form = SignupForm()
#     return render(request, 'generic_forms.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, 'generic_forms.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))