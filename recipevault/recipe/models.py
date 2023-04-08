from django.db import models
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField()
    rating = models.PositiveIntegerField()
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()