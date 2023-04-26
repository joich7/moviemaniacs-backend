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
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Playlist_movie(models.Model):
    playlist_id = models.ForeignKey('Playlist', on_delete=models.CASCADE)
    movie_id = models.IntegerField()
    movie_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.movie_name


class Review(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='movie_review')
    movie_id = models.IntegerField()
    headline = models.CharField(max_length=50, null=True, blank=True)
    movie_rating = models.IntegerField()
    description = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
