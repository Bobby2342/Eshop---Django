from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField()
    password= models.TextField(hash)

class Product (models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='images/')
    imgurl = models.TextField()
    condition = models.CharField(max_length=255)
