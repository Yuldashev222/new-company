from django.forms import ModelForm

from .models import *

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'bio', 'text', 'url', 'active']

