from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mission(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

class Comment(models.Model):
    content = models.CharField(max_length=100)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)

