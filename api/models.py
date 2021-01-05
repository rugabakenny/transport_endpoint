from django.db import models

# Create your models here.
class Posts(models.Model):
    title =models.Charfield(max_length=255)
    posted by =models.models.Charfield(max_length=255)
    description =models.Textfield()
