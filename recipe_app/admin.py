from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from recipe_app.models import Author, RecipeItems

admin.site.register(Author)
admin.site.register(RecipeItems)

class AuthorUserAdmin(UserAdmin):
    model = Author
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('following')}),)