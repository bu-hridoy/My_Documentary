from django.db import models
from django.utils import timezone


# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    poster_name = models.CharField(max_length=40)
    poster_email = models.CharField(max_length=40)
    poster_code = models.CharField(max_length=6)
