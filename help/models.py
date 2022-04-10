from django.db import models

class Help(models.Model):
    task = models.CharField(max_length=35)
    howto = models.TextField(max_length=500, default='')
    video = models.FileField(upload_to='static/videos', blank=True)
    video_type = models.CharField(max_length=6, blank=True)
    def __str__(self):
        return self.task