# Generated by Django 4.2 on 2023-04-30 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviemaniacs', '0006_rename_movie_id_review_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist_movie',
            name='poster',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
