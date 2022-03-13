from django.contrib import admin

from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'category', 'author', 'company', 'date_created', 'date_updated', 'active']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['id', 'author', 'post', 'text', 'date_created', 'date_updated']
