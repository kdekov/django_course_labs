from django.db import models
from django.utils import timezone

# Create your models here.
class Genre(models.Model):
  name = models.CharField(max_length=50)
  notes = models.TextField(null=True,blank=True)

  def __str__(self):
    return self.name

class Artist(models.Model):
  name = models.CharField(max_length=50)
  about = models.TextField()
  birth_date = models.DateField()
  is_fav = models.BooleanField()

class Album(models.Model):
  name = models.CharField(max_length=50)
  date = models.DateTimeField()
  about = models.TextField()
  is_fav = models.BooleanField()
  release_date = models.DateField(null=True)
  genre = models.ManyToManyField(Genre)
  artist = models.ManyToManyField(Artist)

class Track(models.Model):
  name = models.CharField(max_length=50)
  duration = models.BigIntegerField()
  lyrics = models.TextField()
  is_fav = models.BooleanField()
  album = models.ForeignKey(Album,on_delete=models.PROTECT)
  artist = models.ManyToManyField(Artist)
