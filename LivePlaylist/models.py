from django.db import models
from django.utils import timezone

# Create your models here.
class Playlist(models.Model):
    # title =  models.CharField(max_length=150)
    # video_id = models.CharField(max_length=100)
    create_at = models.DateTimeField(default=timezone.now)


class Music(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete = models.CASCADE)
    title =  models.CharField(max_length=150)
    video_id = models.CharField(max_length=100)

    def __str__(self):
        return self.title