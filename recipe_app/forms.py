from django import forms
from recipe_app.models import Author

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'author_name',
            'author_bio'
        ]

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    approx_time = forms.CharField(max_length=20)
    instructions = forms.CharField(widget=forms.Textarea)