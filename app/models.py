from django.db import models

# Create your models here


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.CharField(max_length=100)
    price = models.IntegerField()
    image_url = models.TextField()
    author = models.CharField(max_length=50)


class Order(models.Model):
    total = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
