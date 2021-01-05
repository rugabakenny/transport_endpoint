from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=255)
    description = models.TextField()
