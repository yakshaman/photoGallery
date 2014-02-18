from django.db import models

# Create your models here.

class Album(models.Model): 
    title = models.CharField(max_length=200)
    visible = models.BooleanField()
    date = models.DateField()
    
class Photo(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=200)
    date = models.DateField()
    orig_filename = models.CharField(max_length=200)
    gen_filename = models.CharField(max_length=20)