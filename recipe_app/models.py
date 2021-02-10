from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    author_name = models.CharField(max_length=150)
    author_bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author_name

class RecipeItems(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    approx_time = models.CharField(max_length=20)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} | {self.author}"
