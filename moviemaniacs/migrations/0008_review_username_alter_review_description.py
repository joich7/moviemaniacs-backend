# Generated by Django 4.2 on 2023-05-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviemaniacs', '0007_playlist_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='username',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.CharField(max_length=20),
        ),
    ]