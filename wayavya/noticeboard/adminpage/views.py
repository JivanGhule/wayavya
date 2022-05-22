"""
Team Wayavya
Author - Kiran Kamble
Date Created - 2022-05-18
File name - views.py.- This file has function to render admin html file  
"""


from django.shortcuts import render

# Create your views here.
def adminPage(request):
    return render(request,'admin.html')

def editNoticePage(request):
    return render(request,'noticeedit.html')