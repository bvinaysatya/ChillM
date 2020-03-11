from django.db import models
from django.urls import reverse

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.album_name

    def get_absolute_url(self):
        return reverse('album-home')

class Artist(models.Model):
    artist_name = models.CharField(max_length=100)

    def __str__(self):
        return self.artist_name

class Track(models.Model):
    track_name = models.CharField(max_length=100)
    artist = models.ManyToManyField(Artist)
    #file = models.FileField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.track_name

