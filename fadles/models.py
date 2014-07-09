from django.db import models
from sorl.thumbnail import ImageField
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField

def content_file_name(instance, filename):
    return '/'.join(['content', filename])

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    preview = ImageField(upload_to=content_file_name)
    is_popular = models.BooleanField(default=False)
    start_price = models.IntegerField(default=0)
    unit = models.CharField(max_length=16)
    additional_info = RichTextField()

    def __str__(self):
        return self.name.encode('utf-8')

class ProductImage(models.Model):
    property = models.ForeignKey(Product, related_name='images')
    image = ImageField(upload_to=content_file_name)


class ProductCertificate(models.Model):
    property = models.ForeignKey(Product, related_name='certificates')
    name = name = models.CharField(max_length=256)
    image = ImageField(upload_to=content_file_name)

class House(models.Model):
    name = models.CharField(max_length=512)
    description = RichTextField()
    preview = ImageField(upload_to=content_file_name)

    def __str__(self):
        return self.name.encode('utf-8')

class HouseImage(models.Model):
    property = models.ForeignKey(House, related_name='images')
    image = ImageField(upload_to=content_file_name)

class PopularProduct(models.Model):
    size = models.CharField(max_length=256)
    start_price = models.IntegerField(default=0)
    unit = models.CharField(max_length=16)
    preview = ImageField(upload_to=content_file_name)
    product = models.ForeignKey(Product, related_name='populars')
    is_active = models.BooleanField()

    def __str__(self):
        return self.product.name.encode('utf-8')

    def name(self):
        return self.product.name.encode('utf-8')

class Sale(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    preview = ImageField(upload_to=content_file_name)
    product = models.ForeignKey(Product, related_name='sales')
    is_active = models.BooleanField()

    def __str__(self):
        return self.name.encode('utf-8')

