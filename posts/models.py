import datetime

from django.db import models


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True)
    date = models.DateTimeField()

    @property
    def related_comments(self):
        return self.comments.all()

    def __str__(self):
        return f"movie {self.id}: {self.title}"


class Comments(models.Model):
    voice = models.FileField()
    text = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    movie = models.ForeignKey(
        Movie, blank=True, on_delete=models.CASCADE, related_name='comments', null=True)



    def __str__(self):
        return f"movie {self.id}: {self.text}"
