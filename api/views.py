from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Rating, Movie
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import MovieSerializer, RatingSerializer, UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'rating' in request.data:
            movie = Movie.objects.get(pk=pk)
            user = request.user
            rating = request.data['rating']

            try:
                movie_rating = Rating.objects.get(user=user.id, movie=movie.id)
                movie_rating.rating = rating
                movie_rating.save()
                serializers = RatingSerializer(movie_rating, many=False)
                response = {'message': 'Rating Updated', 'result': serializers.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                movie_rating = Rating.objects.create(user=user, movie=movie, rating = rating)
                serializers = RatingSerializer(movie_rating, many=False)
                response = {'message': 'Rating Created', 'result': serializers.data}
                return Response(response, status=status.HTTP_200_OK)


        else:
            response = {'message': 'ERROR'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def create(self, request, *args, **kwargs):
        response = {'message':'You can not create rating like that'}
        return Response(response, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        response = {'message':'You can not update rating like that'}
        return Response(response, status= status.HTTP_400_BAD_REQUEST)