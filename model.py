from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, default='Pending')
    delivery_person = models.ForeignKey('DeliveryPerson', on_delete=models.SET_NULL, null=True)

class DeliveryPerson(models.Model):
    name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

# Add more models as needed...