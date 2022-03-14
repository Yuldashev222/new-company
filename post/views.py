from django.shortcuts import render


def posts(request):

    context = {
        'title': 'posts'
    }

    return render(request=request, template_name='posts.html', context=context)


def post_detail(request):

    return render(request=request, template_name='post-single.html')