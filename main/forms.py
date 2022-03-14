from django.forms import ModelForm

from .models import *

class CompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'category', 'email', 'tel', 'logotype', 'info', 'telegram_link', 'instagram_link', 'facebook_link', 'state', 'city', 'street', 'url']


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'url']