from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=20, null=True, blank=False)

    def __str__(self):
        return self.title


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(null=True, max_length=20, blank=True)
    music = models.FileField(null=True, upload_to='music/Track/%Y/%m/%d/')

    def __str__(self):
        return '{}-{}'.format(self.album, self.title)
