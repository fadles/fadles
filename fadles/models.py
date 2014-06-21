from django.db import models
from sorl.thumbnail import ImageField

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=2048)
    image = ImageField()