from django.db import models

# Create your models here.
class Playlist(models.Model):
    title =  models.CharField(max_length=150)
    video_id = models.CharField(max_length=100)

    def __str__(self):
        return self.title