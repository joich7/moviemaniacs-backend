# Generated by Django 4.2 on 2023-04-26 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviemaniacs', '0002_playlist_review_playlist_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist_movie',
            name='movie_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]