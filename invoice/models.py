from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True)
    number=models.CharField(max_length=10)
    pincod=models.CharField(max_length=6)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=50)
    house_number=models.CharField(max_length=10)
    Strite=models.CharField(max_length=100)
    password=models.CharField(max_length=20, default='user@123')
    def __str__(self):
        return self.username


class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_discription=models.TextField(max_length=200)
    def __str__(self):
        return self.product_name

class Invoice(models.Model):
    Client_details= models.ForeignKey(User, on_delete=models.CASCADE)
    product_details=models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.IntegerField()
    discount=models.IntegerField(default=0)
    sub_total=models.IntegerField()

    def __str__(self):
        return str(self.Client_details)