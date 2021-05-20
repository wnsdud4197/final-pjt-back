from django.db import models
from django.conf import settings

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Language(models.Model):
    original_language = models.CharField(max_length=10)
    kor_language = models.CharField(max_length=10)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField(default='1909-01-01')
    youtube_key = models.CharField(max_length=50, null=True)
    poster_path = models.CharField(max_length=100, null=True)
    vote_average = models.FloatField()
    genre_ids = models.ManyToManyField(Genre)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    keep_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='keep_movies')
    
class Review(models.Model):
    content = models.TextField()
    rank = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
