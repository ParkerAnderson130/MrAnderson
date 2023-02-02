from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField 

class Post(models.Model):
    GENRES = (
        ('Opinion', 'Opinion'),
        ('Sports', 'Sports'),
        ('Tech', 'Technology'),
    )
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    genre = models.CharField(choices=GENRES, default="Opinion", max_length=300)
    body = HTMLField(default="Mr. Anderson is working on this one.")
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

