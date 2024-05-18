from django.db import models
from accounts.models import User

# Create your models here.
class Products(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    company=models.CharField(max_length=30)
    quantity=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    image1=models.CharField(max_length=30)
    image2=models.CharField(max_length=30)
    image3=models.CharField(max_length=30)