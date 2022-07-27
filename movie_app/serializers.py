from movie_app.models import Director, Movie, Review
from rest_framework import serializers


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()
        # exlcude = 'description duration director'.split()

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'title description duration director reviews'.split()




