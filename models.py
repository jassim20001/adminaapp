from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    date=models.DateField()
    about=models.TextField(max_length=1000)
    rate=models.IntegerField()
    slug=models.SlugField()
    img=models.ImageField(upload_to='photo')
