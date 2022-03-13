from django.contrib import admin

from .models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'author', 'category', 'email']

