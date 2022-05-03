from django.contrib import admin
from django.urls import path
from .views import learn

urlpatterns = [
    path('', learn),
]
