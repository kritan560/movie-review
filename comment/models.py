from django.db import models
from movie_list.models import Movie
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comments = models.TextField()
