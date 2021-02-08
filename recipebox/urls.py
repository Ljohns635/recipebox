"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipe_app.views import index_view, recipe_details, author_details, add_author, add_recipe

urlpatterns = [
    path('', index_view, name='homepage'),
    path('recipes/<int:post_id>/', recipe_details, name='recipe_details'),
    path('authors/<int:author_id>/', author_details, name='author_details'),
    path('recipe/addrecipe/', add_recipe, name='add_recipe'),
    path('author/addauthor/', add_author, name='add_author'),
    path('admin/', admin.site.urls),
]