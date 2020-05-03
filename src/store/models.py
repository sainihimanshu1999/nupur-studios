from django.db import models
from django.conf import settings

class Profile(models.Model):
    firstname  = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    notes = models.TextField(max_length=255)
    twitter = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    google = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='profile_image', blank = True)

    def __str__(self):
        return self.firstname