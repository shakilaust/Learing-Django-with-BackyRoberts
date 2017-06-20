from django.db import models

# red pk 1
class Album(models.Model):
    artist = models.CharField(max_length=250)
    albumTitle = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    albumLogo = models.CharField(max_length=1000)
    def __str__(self):
        return self.albumTitle + ' ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    fileType = models.CharField(max_length=100)
    songTitle = models.CharField(max_length=250)
    isfavorite = models.BooleanField(default=False)
    def __str__(self):
        return self.songTitle