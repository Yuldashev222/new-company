from unicodedata import name
from django.urls import path
from .views import *

from post.views import *
from product.views import *
from account.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('about/team/', team, name='team'),
    path('about/team/testimonials/', testimonials, name='testimonials'),
    path('services/', services, name='services'),
    path('pricing/', pricing, name='pricing'),
    path('contact/', contact, name='contact'),

    path('delete-company/<slug:url>/', delete_company, name='delete_company'), 
    path('single-company/<slug:url>/', single_company, name='single-company'),

    # Product views //////////////////
    path('products/', products, name='products'),

    # Post views //////////////////
    path('posts/', posts, name='posts'),
    path('post-single/', post_detail, name='post-detail'),

    # Account views //////////////////
    path('profile-User/<str:username>/', profile_user, name='user-profile'),
    path('profile-Employee/<str:username>/', profile_employee, name='user-employee'),
    path('Registration/', user_registration, name='registration'),
    path('login/', user_login, name='login'),
    path('home/', user_logout, name='logout'),
]
