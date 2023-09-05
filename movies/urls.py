from django.urls import path
from .views import CreateListMoviesView, MoviesDetailsView, MoviesOrderView

urlpatterns = [
    path('movies/', CreateListMoviesView.as_view()),
    path('movies/<int:movie_id>/', MoviesDetailsView.as_view()),
    path('movies/<int:movie_id>/orders/', MoviesOrderView.as_view()),
]
