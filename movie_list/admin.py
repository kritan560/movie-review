from django.contrib import admin
from . models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_name', 'movie_image']
    