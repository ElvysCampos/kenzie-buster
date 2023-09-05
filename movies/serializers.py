from rest_framework import serializers
from .models import Movie, CategorySize, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=127)

    duration = serializers.CharField(
        max_length=10, allow_null=True, default=None)

    rating = serializers.ChoiceField(
        choices=CategorySize.choices, default=CategorySize.size_g
    )
    synopsis = serializers.CharField(allow_null=True, default=None)

    added_by = serializers.EmailField(source='user.email', read_only=True)

    def create(self, validated_data):
        serializers = Movie.objects.create(**validated_data)
        return serializers


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(
        max_length=127, source='movie.title', read_only=True)

    buyed_by = serializers.EmailField(read_only=True, source='user.email')

    buyed_at = serializers.DateTimeField(read_only=True)

    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    def create(self, validated_data):
        serializers = MovieOrder.objects.create(**validated_data)
        return serializers
