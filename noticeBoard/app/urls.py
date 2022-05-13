# Team - Wayavya
# Author - Kiran Kamble
# Date created - 2022-05-12
# File Name - urls.py (This file contain urls to visit login, signup and home page)

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('home/',views.homePage),
    
    
]
