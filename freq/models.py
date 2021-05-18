from django.db import models

# Create your models here.

class Words(models.Model):
    URL = models.CharField(max_length=200)
    data = models.TextField()