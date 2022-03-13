from django.shortcuts import redirect, render
from django.contrib.auth import login, logout


def profile_user(request):

    return render(request, 'profile_user.html')


def profile_employee(request):

    return render(request, 'profile_employee.html')


def profile_director(request):

    return render(request, 'profile_director.html')


def user_registration(request):

    return render(request, 'register.html')


def user_login(request):

    return render(request, 'login.html')


def user_logout(request):

    logout(request)

    return redirect('home')