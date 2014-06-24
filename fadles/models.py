from django.db import models
from sorl.thumbnail import ImageField

def content_file_name(instance, filename):
    return '/'.join(['content', filename])

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=2048)
    image = ImageField(upload_to=content_file_name)