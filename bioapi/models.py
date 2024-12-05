from django.db import models
from datetime import datetime


class Photo(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=True, blank=True)
    likes = models.IntegerField(default = 0)
    
    def __str__(self):
        return f"{self.title} - {self.location} - {self.likes}"
    


class Album(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    pub_date = models.DateTimeField(default = datetime.now)
    photos = models.ManyToManyField(Photo)

    def __str__(self):
        return f"{self.title} - {self.pub_date}"
