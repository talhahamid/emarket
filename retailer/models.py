from django.db import models
from accounts.models import User
from distributor.models import Products
# Create your models here.
class Bought(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    owner=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    company=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    quantity=models.CharField(max_length=30)
    boughtquantity=models.CharField(max_length=30)

class Orders(models.Model):
    name=models.CharField(max_length=30)
    quantity=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    totalprice=models.CharField(max_length=30)
    owner=models.CharField(max_length=30)
    buyer=models.CharField(max_length=30)
    ordered=models.BooleanField(default=False)
