from django.db import models

class payment(models.Model):
    order_id = models.CharField(max_length=50)
    card_number = models.CharField(max_length=50)
    expiration_date = models.CharField(max_length=50)
    cvc = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
