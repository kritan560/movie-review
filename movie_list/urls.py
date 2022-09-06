from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='movie-homepage'),
    path('movie/create-movie/', views.CreateMovieList.as_view(), name='create-movie'),
    path('movie/<int:pk>/detail', views.MovieDetailView.as_view(), name='movie-detail'),
    path('search/', views.SearchPageview.as_view(), name='search-movie'),
]