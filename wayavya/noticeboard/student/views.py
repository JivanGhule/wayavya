"""
Team Wayavya
Author - Kiran Kamble
Date Created - 2022-05-18
File name - views.py.- This file has function to render the student & Faculty html file  
"""

from django.shortcuts import render

# Create your views here.
def studentPage(request):
    return render(request,'student.html')

def teacherPage(request):
    return render(request,'teacher.html')