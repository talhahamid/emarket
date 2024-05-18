from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100, unique=True)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    ROLE_CHOICES = (
        ('distributor', 'Distributor'),
        ('retailer', 'Retailer'),
    )
    role=models.CharField(max_length=100,choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)


class Profilepic(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profilepic=models.CharField(max_length=100)    