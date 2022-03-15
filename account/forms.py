from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import *

class UserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'photo', 'bio',]


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class UserCreateFormAdd_in_Profile(UserCreationForm):

    class Meta:
        model = User
        fields = ['username']


class AddEmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = ['name', 'position', 'email', 'tel', 'photo', 'bio', 'telegram_link', 'instagram_link', 'facebook_link', 'state', 'city', 'street', 'url', 'active']


class EditEmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = ['name', 'email', 'tel', 'photo', 'bio', 'telegram_link', 'instagram_link', 'facebook_link', 'state', 'city', 'street', 'url']