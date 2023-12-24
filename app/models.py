from collections.abc import Iterable
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField()
    password= models.TextField()
    confirmpassword = models.TextField()

class Product (models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='images/')
    imgurl = models.TextField()
    condition = models.CharField(max_length=255)
    categories = models.CharField(max_length=255)

    def similar_products(self):
        return Product.objects.filter(categories=self.categories).exclude(id=self.id)
    

class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField( max_length=255)

    subject = models.TextField()

    message = models.TextField()

    
    def save(self, *args, **kwargs):
        super(Contact, self).save(*args, **kwargs)

class Cart (models.Model):

    name = models.CharField( max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    

