from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('account',views.account,name='account'),
    path('contact',views.contact,name='contact'),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('signout',views.signout,name='signout'),
    path('signup',views.signup,name='signup'),
    path('navbar',views.navbar,name='navbar'), 
    path('sitemap',views.sitemap,name='sitemap'), 
    path('sitemap.xml',views.sitemap,name='sitemap'), 
    path('ads',views.ads,name='ads'), 
    path('ads.txt',views.ads,name='ads'), 
    path('Ads',views.ads,name='ads'), 
    path('Ads.txt',views.ads,name='ads'), 
]