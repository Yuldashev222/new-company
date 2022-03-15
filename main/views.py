from django.shortcuts import redirect, render

from account.models import Employee
from main.forms import CompanyForm
from main.models import Company
from post.models import Post
from product.models import Product, Product_image

from account.forms import *
from post.forms import *
from product.forms import *


def home(request):

    context = {
        'title': 'home'
    }

    return render(request=request, template_name='index.html', context=context)


def about(request):

    context = {
        'title': 'about us'
    }

    return render(request=request, template_name='about.html', context=context)


def testimonials(request):

    context = {
        'title': 'testimonials'
    }

    return render(request=request, template_name='testimonials.html', context=context)


def team(request):

    context = {
        'title': 'team'
    }

    return render(request=request, template_name='team.html', context=context)


def services(request):

    context = {
        'title': 'services'
    }

    return render(request=request, template_name='services.html', context=context)


def pricing(request):

    context = {
        'title': 'pricing'
    }

    return render(request=request, template_name='pricing.html', context=context)


def contact(request):

    context = {
        'title': 'contact'
    }

    return render(request=request, template_name='contact.html', context=context)


def delete_company(request, url):
    company = Company.objects.get(url=url)
    user = company.author

    company.delete()

    try:
        return redirect('user-employee', user.employee.url)

    except:
        return redirect('user-profile', user.username)



def single_company(request, url):
    company = Company.objects.get(url=url)
    employes = Employee.objects.filter(company=company)
    posts = Post.objects.filter(company=company)
    products = Product.objects.filter(company=company)

    EmployeeForm = AddEmployeeForm()
    AddUserForm = UserCreateFormAdd_in_Profile()
    AddPostForm = PostForm()
    AddProductForm = ProductForm()
    EditCompanyForm = CompanyForm(instance=company)

    if request.POST:
        EditCompanyForm = CompanyForm(request.POST, request.FILES, instance=company)

        EmployeeForm = AddEmployeeForm(request.POST or None, request.FILES)
        AddUserForm = UserCreateFormAdd_in_Profile(request.POST)
        AddPostForm = PostForm(request.POST, request.FILES)
        AddProductForm = ProductForm(request.POST, request.FILES)

        if EditCompanyForm.is_valid():
            obj = EditCompanyForm.save(commit=False)
            obj.save()

            return redirect('single-company', obj.url)


        if EmployeeForm.is_valid() and AddUserForm.is_valid():
            obj = EmployeeForm.save(commit=False)
            obj_user = AddUserForm.save(commit=False)
            obj.user = obj_user
            obj.company = company
            obj_user.save()
            obj.save()

            return redirect('single-company', url)


        if AddPostForm.is_valid():
            obj = AddPostForm.save(commit=False)
            obj.company = company
            obj.author = company.author
            obj.save()
            AddPostForm.save_m2m()

            return redirect('single-company', url)


        if AddProductForm.is_valid():
            obj = AddProductForm.save(commit=False)
            obj.company = company
            obj.author = company.author
            obj.save()
        
            return redirect('single-company', url)


    context = {

        'company': company,
        'employes': employes,
        'posts': posts,
        'products': products,

        'EditCompanyForm': EditCompanyForm,

        'AddEmployeeForm': EmployeeForm,        
        'AddUserForm': AddUserForm,
        'AddPostForm': AddPostForm,
        'AddProductForm': AddProductForm,        
    }

    return render(request=request, template_name='single_company.html', context=context)

