from django.urls import path
from . import views

urlpatterns = [
    path('home page/',views.homePage),
    path('signup/',views.signupPage),
    path('our team/',views.teamPage),
]
