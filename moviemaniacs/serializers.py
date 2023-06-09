from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser, Playlist, Review, Playlist_movie


class UserPlaylistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'user', 'title',]


class Playlist_MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist_movie
        fields = ['id', 'playlist', 'movie_id', 'movie_name', 'poster']


class PlaylistSerializer(serializers.ModelSerializer):
    movies = Playlist_MoviesSerializer(many=True, required=True)

    class Meta:
        model = Playlist
        fields = ['id', 'user', 'title', 'list_type', 'movies']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'title', 'user']


class PlaylistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['user', 'title', 'list_type']


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password',
                  'first_name', 'last_name',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        playlist = Playlist.objects.create(
            user=instance, title=f"{instance.first_name}'s Favorites", list_type="f")
        playlist = Playlist.objects.create(
            user=instance, title=f"{instance.first_name}'s Watchlist", list_type="w")
        return instance

# class UserReadSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'username', 'first_name', 'last_name', )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'movie', 'headline',
                  'movie_rating', 'description', 'date_posted', 'username']
