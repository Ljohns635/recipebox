from django import forms
from recipe_app.models import Author

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'author_name',
            'author_bio',
            'user'
        ]

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    # author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=150)
    approx_time = forms.CharField(max_length=20)
    instructions = forms.CharField(widget=forms.Textarea)

# class SignupForm(forms.Form):
#     author_name = forms.CharField(max_length=150)
#     author_bio = forms.CharField(widget=forms.Textarea)
#     username = forms.CharField(max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)