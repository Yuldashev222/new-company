from django.shortcuts import render


def posts(request):

    return render(request, 'posts.html')
    

def post_detail(request):

    return render(request, 'post-single.html')