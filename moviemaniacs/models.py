from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

# Create your models here.


class Playlist(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # type of playlist for filtering(f=favorites, c=custom(what user will be making), w= watchlist) creates custom on default
    list_type = models.CharField(max_length=1, default="c")

    def __str__(self):
        return self.title


class Playlist_movie(models.Model):
    playlist = models.ForeignKey(
        'Playlist', on_delete=models.CASCADE, related_name="movies", null=True, blank=True)
    movie_id = models.IntegerField()
    movie_name = models.CharField(max_length=50, null=True, blank=True)
    poster = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.movie_name


class Review(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='movie_review')
    movie = models.IntegerField()
    username = models.CharField(max_length=20, null=True, blank=True)
    headline = models.CharField(max_length=50, null=True, blank=True)
    movie_rating = models.IntegerField()
    description = models.CharField(max_length=300)
    date_posted = models.DateTimeField(auto_now_add=True)
