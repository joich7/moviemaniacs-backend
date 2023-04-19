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
    title = models.CharField(max_length=50, null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_id = models.IntegerField(null=True)
    
