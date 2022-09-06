from django.shortcuts import render, redirect
from .models import Movie
from django.views.generic import (
    View,
    CreateView,
    DetailView,
)
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from comment.models import Comment

# Create your views here.

class HomePageView(View):
    def get(self, request):
        movie = Movie.objects.all()
        context = {'movies':movie}
        return render(request, 'apps/movie-list/movie.html', context)

class SearchPageview(View):
    def get(self, request):
        keyword = request.GET.get('search')
        if keyword:
            filtered_movie = Movie.objects.filter(movie_name__icontains=keyword)
        else:
            filtered_movie = Movie.objects.all()
        context = {'movies':filtered_movie}
        return render(request, 'apps/movie-list/search-movie/search-movie.html', context)

class CreateMovieList(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['movie_name', 'movie_detail', 'movie_image']
    template_name = 'apps/movie-list/create-movie/create-movie.html'
    success_url = reverse_lazy('movie-homepage')

class MovieDetailView(View):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        comment = Comment.objects.filter(name=movie)
        context = {'movie':movie, 'comment':comment}
        return render(request, 'apps/movie-list/detail-movie/detail-movie.html', context)

    def post(self, request, pk):
        movie= Movie.objects.get(pk=pk)
        posted_comment = request.POST['comment']
        Comment.objects.create(comments=posted_comment, name=movie)
        return redirect('movie-detail', pk)