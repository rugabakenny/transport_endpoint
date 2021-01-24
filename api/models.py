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

class Transfer(models.Model):
    sentfrom =models.CharField(max_length=244)
    sendto = models.CharField(max_length=255)
    amount = models.CharField(max_length=100)
    
    def _str_(self):
        return self.amount
