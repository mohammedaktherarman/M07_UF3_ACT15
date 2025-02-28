from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50) 

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    total_price = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)

class Payment(models.Model):
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)
    cvc = models.CharField(max_length=3)