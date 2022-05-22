from django.urls import path
from . import views

urlpatterns = [
    path('student notices/',views.studentPage),
    path('teacher notices/',views.teacherPage),
]
