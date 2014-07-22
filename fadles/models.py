# -*- coding: utf-8 -*-
import csv
import json
from django.db import models
from sorl.thumbnail import ImageField
import time
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
    product = models.ForeignKey(Product, related_name='images')
    image = ImageField(upload_to=content_file_name)


class ProductCertificate(models.Model):
    product = models.ForeignKey(Product, related_name='certificates')
    name = name = models.CharField(max_length=256)
    image = ImageField(upload_to=content_file_name)

class House(models.Model):
    name = models.CharField(max_length=512)
    description = RichTextField()
    preview = ImageField(upload_to=content_file_name)

    def __str__(self):
        return self.name.encode('utf-8')

class HouseImage(models.Model):
    product = models.ForeignKey(House, related_name='images')
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

class ProductTable(models.Model):
    product = models.ForeignKey(Product, related_name='tables')
    name = models.CharField(max_length=256)
    table_json = models.TextField()
    table = models.FileField(upload_to=content_file_name)

    def __str__(self):
        return self.name.encode('utf-8')

    def save(self, *args, **kwargs):
        ts = time.time()
        self.table.name = '%s.csv' % ts
        super(ProductTable, self).save(*args, **kwargs)

        with open(self.table.path, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            res = []
            for row in spamreader:
                json_row = {}
                i = 0
                for string in row:
                    line = string.decode('cp1251')
                    json_row[i] = line
                    i += 1
                res.append(json_row)

            self.table_json = json.dumps(res,ensure_ascii=False)

        super(ProductTable, self).save(*args, **kwargs)

class ContactUs(models.Model):
    name = models.CharField(max_length=256)
    email_or_phone = models.CharField(max_length=256)
    message = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    preview = ImageField(upload_to=content_file_name)
    review = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    moderated = models.BooleanField(default=False)
