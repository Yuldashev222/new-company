from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import authenticate

from .models import *
from main.models import *

from .forms import *
from main.forms import *
from post.forms import *
from product.forms import *


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


def profile_employee(request, url):
    employee = Employee.objects.get(url=url)

    company = employee.company
    companies = Company.objects.filter(author=employee.user)
    posts = Post.objects.filter(author=employee.user)
    products = Product.objects.filter(author=employee.user)

    EmpEditForm = EditEmployeeForm(instance=employee)
    AddCompanyForm = CompanyForm()
    AddPostForm = PostForm()
    AddProductForm = ProductForm()

    if request.POST:
        AddCompanyForm = CompanyForm(request.POST, request.FILES)
        EmpEditForm = EditEmployeeForm(request.POST, request.FILES, instance=employee)
        AddPostForm = PostForm(request.POST, request.FILES)
        AddProductForm = ProductForm(request.POST, request.FILES)


        if AddCompanyForm.is_valid():
            obj = AddCompanyForm.save(commit=False)
            obj.author = employee.user
            obj.save()

            return redirect('user-employee', url)


        if EmpEditForm.is_valid():
            obj = EmpEditForm.save(commit=False)
            obj.save()

            return redirect('user-employee', obj.url)


        if AddPostForm.is_valid():
            obj = AddPostForm.save(commit=False)
            obj.company = employee.company
            obj.author = employee.user
            obj.save()
            AddPostForm.save_m2m()

            return redirect('user-employee', url)


        if AddProductForm.is_valid():
            obj = AddProductForm.save(commit=False)
            obj.company = employee.company
            obj.author = employee.user
            obj.save()
        
            return redirect('user-employee', url)


    context = {
        'employee': employee,
        'companies': companies,
        'company': company,
        'posts': posts,
        'products': products,    

        'EmpEditForm': EmpEditForm,
        'AddCompanyForm': AddCompanyForm,
        'AddPostForm': AddPostForm,
        'AddProductForm': AddProductForm,
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