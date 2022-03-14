from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import authenticate

from .models import *
from .forms import *
from main.forms import *
from main.models import *


def profile_user(request, username):

    user = User.objects.get(username=username)
    companies = Company.objects.filter(author=user)

    UserEditForm = UserForm(instance=user)

    AddCompanyForm = CompanyForm()

    category_form = CategoryForm()


    if request.POST:
        UserEditForm = UserForm(request.POST, request.FILES, instance=user)

        if UserEditForm.is_valid():
            obj = UserEditForm.save(commit=False)
            obj.save()

            messages.success(request, 'Profile muvaffaqqiyatli o\'zgartirildi')

            return redirect('user-profile', obj.username)


    if request.POST:
        AddCompanyForm = CompanyForm(request.POST, request.FILES)

        if AddCompanyForm.is_valid():
            obj = AddCompanyForm.save(commit=False)
            obj.author = user
            obj.save()

            messages.success(request, 'Companiya muvaffaqqiyatli qo\'shildi')
            
            return redirect('user-profile', username)


        elif not AddCompanyForm.category and category_form.is_valid():
            category_form = CategoryForm(request.POST)
            
            AddCompanyForm.category = category_form

            if AddCompanyForm.is_valid():
                obj = AddCompanyForm.save(commit=False)
                obj_cat = category_form.save(commit=False)
                obj.author = user
                obj_cat.save()
                obj.save()

                messages.success(request, 'Companiya muvaffaqqiyatli qo\'shildi')
                
        else:
            messages.error(request, 'Companiyani xato toldirdingiz')
    
        return redirect('user-profile', username)


    context = {

        'user': user,
        'companies': companies,

        'User_edit_form': UserEditForm,

        'AddCompanyForm': AddCompanyForm,

        'category_form': category_form,
        
    }

    return render(request=request, template_name='profile_user.html', context=context)


def profile_employee(request, username):

    context = {
        
    }

    return render(request=request, template_name='profile_employee.html', context=context)

def user_registration(request):

    user_create_form = UserCreateForm()

    if request.POST:
        user_create_form = UserCreateForm(request.POST)

        if user_create_form.is_valid():
            obj = user_create_form.save(commit=False)
            obj.save()

            return redirect('login')


    context = {
        
    }

    return render(request=request, template_name='register.html', context=context)


def user_login(request):

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            return redirect('home')
        
        else:

            messages.error(request, 'Login yoki parol xato')


    return render(request=request, template_name='login.html')


def user_logout(request):

    logout(request)

    return redirect('home')