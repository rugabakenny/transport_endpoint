from django.db import models

# Create your models here.
class Postnews(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    location =models.CharField(max_length=255)
    image = models.ImageField()
    price =models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title

class Gorilla(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    location =models.CharField(max_length=255)
    image = models.ImageField()
    price =models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title


class Lake(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    location =models.CharField(max_length=255)
    image = models.ImageField()
    price =models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title

class Hotel(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    location =models.CharField(max_length=255)
    image = models.ImageField()
    price =models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title
class Mountain(models.Model):
    title = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    location =models.CharField(max_length=255)
    image = models.ImageField()
    price =models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title


