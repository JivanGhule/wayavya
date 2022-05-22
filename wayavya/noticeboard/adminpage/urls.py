from django.urls import path
from . import views

urlpatterns = [
    path('admin page/',views.adminPage),
    path('admin2 page/',views.editNoticePage),
]