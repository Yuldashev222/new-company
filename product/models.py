from django.db import models

from main.models import *
from account.models import *


class Product(models.Model):
    company = models.ForeignKey(Company, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='products', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(help_text='Dollarda kirgizing!!!')
    bio = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    url = models.SlugField(unique=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product_image(models.Model):
    product = models.ManyToManyField(Product, related_name='images')
    image = models.ImageField(upload_to='Product images/')
    desc = models.CharField(max_length=200, blank=True, null=True)


