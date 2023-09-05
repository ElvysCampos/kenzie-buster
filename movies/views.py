from rest_framework.views import Response, Request, status, APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrReadOnly
from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer, MovieOrderSerializer
from .models import Movie
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


class CreateListMoviesView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def post(self, request: Request):

        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        users = request.user

        serializer.save(user=users)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request):

        movies = Movie.objects.all()

        pagination_movies = self.paginate_queryset(movies, request)

        serializer = MovieSerializer(pagination_movies, many=True)

        return self.get_paginated_response(serializer.data)


class MoviesDetailsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request, movie_id) -> Response:

        movies = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(movies)

        return Response(serializer.data)

    def delete(self, request: Request, movie_id) -> Response:

        movies = get_object_or_404(Movie, id=movie_id)

        movies.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MoviesOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int) -> Response:
        movie_verificay = get_object_or_404(Movie, id=movie_id)

        serializer = MovieOrderSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        users = request.user

        movies = movie_verificay

        serializer.save(movie=movies, user=users)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
