from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
# Create your models here.
class Playlist(models.Model):
    title = models.CharField(max_length=50, null=True)
    # user_id

