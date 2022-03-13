from django.shortcuts import render


def home(request):

    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')

def testimonials(request):

    return render(request, 'testimonials.html')

def team(request):

    return render(request, 'team.html')

def services(request):

    return render(request, 'services.html')

def pricing(request):

    return render(request, 'pricing.html')

def contact(request):

    return render(request, 'contact.html')