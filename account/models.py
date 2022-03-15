from django.db import models
from django.contrib.auth.models import AbstractUser

from main.models import *


class User(AbstractUser):
    photo = models.ImageField(upload_to='User images/', blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.username


class Employee(models.Model):

    position__choices = [
        ('Pt', 'Post admin'),
        ('Pr', 'Product admin')
    ]

    company = models.ForeignKey('main.Company', related_name='employes', on_delete=models.CASCADE)
    user = models.OneToOneField(User, related_name='employee', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=2, choices=position__choices)
    email = models.EmailField(max_length=200, blank=True, null=True)
    tel = models.CharField(max_length=11, blank=True, null=True)
    photo = models.ImageField(upload_to='Employee images/', blank=True, null=True)
    bio = models.CharField(max_length=300, blank=True, null=True)
    telegram_link = models.URLField(max_length=200, blank=True, null=True)
    instagram_link = models.URLField(max_length=200, blank=True, null=True)
    facebook_link = models.URLField(max_length=200, blank=True, null=True)
    state = models.CharField(verbose_name='Viloyat', max_length=300)
    city = models.CharField(verbose_name='shahar', max_length=300)
    street = models.CharField(verbose_name='ko\'cha', max_length=300, blank=True, null=True)
    url = models.SlugField(max_length=200, unique=True)
    active = models.BooleanField(verbose_name='Xolati')
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employes'



