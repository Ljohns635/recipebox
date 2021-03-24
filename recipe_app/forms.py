from django import forms
from recipe_app.models import Author

class AddRecipeForm(forms.Form):
    title = forms.CharField(
        max_length=50,
        label="Title",
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    # author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(
        max_length=150,
        label="Description",
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    approx_time = forms.CharField(
        max_length=20,
        label="Approx time",
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    instructions = forms.CharField(
        label="Instructions",
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        )

class AddAuthorForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
    author_name = forms.CharField(
        max_length=150,
        label="Author name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    author_bio = forms.CharField(
        label="Author bio",
        widget=forms.Textarea(attrs={'class': 'form-control'})
        )


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )