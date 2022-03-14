from django.contrib import admin

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'price', 'bio', 'author', 'company', 'date_created', 'date_updated', 'active']


@admin.register(Product_image)
class ProductImageAdmin(admin.ModelAdmin):
  list_display = ['id', 'image', 'desc']

