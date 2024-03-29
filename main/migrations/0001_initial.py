# Generated by Django 4.0.3 on 2022-03-15 03:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('url', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('tel', models.CharField(blank=True, max_length=11, null=True)),
                ('logotype', models.ImageField(blank=True, null=True, upload_to='Company logos/')),
                ('info', models.TextField()),
                ('telegram_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('state', models.CharField(max_length=300, verbose_name='Viloyat')),
                ('city', models.CharField(max_length=300, verbose_name='shahar')),
                ('street', models.CharField(blank=True, max_length=300, null=True, verbose_name="ko'cha")),
                ('url', models.SlugField(max_length=200, unique=True)),
                ('date_created', models.DateField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='main.category')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
    ]
