from django.db import models

from account.models import *


class Category(models.Model):
    name = models.CharField(max_length=200)
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Company(models.Model):
    author = models.ForeignKey(User, related_name='companies', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='companies', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    tel = models.CharField(max_length=11, blank=True, null=True)
    info = models.TextField()
    telegram_link = models.URLField(max_length=200, blank=True, null=True)
    instagram_link = models.URLField(max_length=200, blank=True, null=True)
    facebook_link = models.URLField(max_length=200, blank=True, null=True)
    state = models.CharField(verbose_name='Viloyat', max_length=300)
    city = models.CharField(verbose_name='shahar', max_length=300)
    street = models.CharField(verbose_name='ko\'cha', max_length=300, blank=True, null=True)
    url = models.SlugField(max_length=200, unique=True)
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'