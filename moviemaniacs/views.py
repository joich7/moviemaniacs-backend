from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import CustomUser, Playlist, Playlist_movie, Review
from .serializers import CustomUserSerializer, PlaylistSerializer, Playlist_MoviesSerializer, ReviewSerializer, PlaylistWriteSerializer
import requests
from django.http import JsonResponse
from django.shortcuts import render
from requests.auth import HTTPBasicAuth
from rest_framework import filters


def send_json(request, searchParam):
    apikey = "apikey=785850a5"
    url = f'https://www.omdbapi.com/?{apikey}{searchParam}'
    # url = f"https://api.github.com/{msg}"
    r = requests.get(url)
    data = r.json()
    # data = [{'name': 'Peter', 'email': 'peter@example.org'},
    #        {'name': 'Julia', 'email': 'julia@example.org'}]
    print(data)
    return JsonResponse(data, safe=False)


class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# class UserPlaylistsViewSet(generics.ListAPIView):
#     queryset = Playlist.objects.all()
#     serializer_class = UserPlaylistsSerializer

#     def get_queryset(self, *args, **kwargs):
#         """
#         This view should return a list of all the purchases for
#         the user as determined by the username portion of the URL.
#         """
#         id = self.kwargs['id']
#         return Playlist.objects.filter(user=user)

class PlaylistWriteViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistWriteSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        queryset = Playlist.objects.all()

        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.filter(user=user)

        movie_id = self.request.query_params.get('boof')
        if movie_id is not None:
            queryset = queryset.filter(user=movie_id)
        return queryset


class favoriteViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.filter(list_type="f")
    serializer_class = PlaylistSerializer


class Playlist_MoviesViewSet(viewsets.ModelViewSet):
    queryset = Playlist_movie.objects.all()
    serializer_class = Playlist_MoviesSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()

        movie_id = self.request.query_params.get('movie')
        if movie_id is not None:
            queryset = queryset.filter(movie=movie_id)
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset
