from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_detail = models.TextField()
    movie_image = models.ImageField(upload_to='movie-list/images/')

    def __str__(self):
        return self.movie_name
