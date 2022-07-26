from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Director, Movie,Review
from movie_app.serializers import DirectorSerializer
from movie_app.serializers import MovieSerializer
from movie_app.serializers import ReviewSerializer




@api_view(['GET'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)


@api_view(['GET'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)


@api_view(['GET'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data)


