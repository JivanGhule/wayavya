# Team - Wayavya
# Author - Kiran Kamble
# Date created - 2022-05-12
# File Name - views.py (This file contain functions to render to html file)

from django.shortcuts import render

USER_NAME = "Kiran Kamble"
USER_EMAIL = "kiran1999kamble@gmail.com"
PASSWORD = "abc123"

# Create your views here.

# Function to visit sign up page
def signup(request):
     # Check if a request is POST
    if (request.method == "POST"):
        #print(request.POST)
        name_data = request.POST["name"]
        email_data = request.POST["email"]
        password_data = request.POST["password"]
        print(name_data)
        print(email_data)
        print(password_data)


        # Need to verify from the Database
        if (name_data != USER_NAME):
            if (email_data != USER_EMAIL ):
                if (password_data != PASSWORD):
                    print("SIGNUP SUCCESSFUL")
                    return render(request,'home.html')
                
                else:
                    print("Password already taken")
            
            else:
                print("Email already exists")
                return render(request,'signup.html')
            
        else:
            print("User name already exists")
            return render(request,'signup.html')
        
    return render(request,'signup.html')

# Function to visit login page
def login(request):
    # Check if a request is POST
    if (request.method == "POST"):
        #print(request.POST)

        email_data = request.POST["email"]
        password_data = request.POST["password"]
        print(email_data)
        print(password_data)


        # Need to verify from the Database

        if (email_data == USER_EMAIL):
            if (password_data == PASSWORD):
                print("LOGIN SUCCESSFUL")
                return render(request,'home.html')
            
            else:
                print("INCORRECT PASSWORD")
                return render(request,'login.html')

        else:
            print("INCORRECT EMAIL")
            return render(request,'login.html')

    return render(request,'login.html')  


# Function to visit Home Page
def homePage(request):
    return render(request,'home.html')

