from django.shortcuts import render


def products(request):

    context = {
        'title': 'products'
    }

    return render(request=request, template_name='products.html', context=context)

