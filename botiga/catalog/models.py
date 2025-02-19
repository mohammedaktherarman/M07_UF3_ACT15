from django.db import models

class product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
