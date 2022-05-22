"""
Team Wayavya
Author - Kiran Kamble
Date Created - 2022-05-18
File name - views.py.- This file has function to render the homepage, signup, our team html file  
"""
from django.shortcuts import render
from django.http import HttpResponse

USER_NAME = "Kiran Kamble"
USER_EMAIL = "kiran1999kamble@gmail.com"
PASSWORD = "abc123"

USER_CLG = "Jagadambha College of Engineering & Technology"
USER_BRANCH = "Electrical Engineering"
USER_WHATSAPP = 9307685205

# Create your views here.
def homePage(request):
    
    # Check if a request is POST
    if (request.method == "POST"):
        #print(request.POST)

        name_data = request.POST["name"]
        email_data = request.POST["email"]
        password_data = request.POST["password"]
        role_data = request.POST["role"]
        print(email_data)
        print(password_data)


        # Need to verify from the Database
        if (email_data == USER_EMAIL):
            if (password_data == PASSWORD):
                if role_data == "Student":
                    print("LOGIN SUCCESSFUL")
                    return render(request,'student.html')
                elif role_data == "Faculty":
                    print("LOGIN SUCCESSFUL")
                    return render(request,'teacher.html')
                elif role_data == "Admin":
                    print("LOGIN SUCCESSFUL")
                    return render(request,'admin.html')

            else:
                print("INCORRECT PASSWORD")
                return render(request,'homepage.html')

        else:
            print("INCORRECT EMAIL")
            return render(request,'homepage.html')

    return render(request,'homepage.html')  

def signupPage(request):

    # Check if a request is POST
    if (request.method == "POST"):
        #print(request.POST)

        name_data = request.POST["name"]
        college_data = request.POST["college"]
        branch_data = request.POST["branch"]
        whatsapp_data = request.POST["phone"]
        email_data = request.POST["email"]
        password_data = request.POST["password"]
        role_data = request.POST["role"]
        print(email_data)
        print(password_data)


        # Need to verify from the Database
        if (college_data == USER_CLG):
            if (whatsapp_data != USER_WHATSAPP):
                if (email_data != USER_EMAIL):
                    if (password_data != PASSWORD):
                        if (role_data == "Student"):
                            print("REGISTRATION SUCCESSFUL")
                            return render(request,'student.html')
                        elif (role_data == "Faculty"):
                            print("REGISTRATION SUCCESSFUL")
                            return render(request,'teacher.html')
                        elif (role_data == "Admin"):
                            print("REGISTRATION SUCCESSFUL")
                            return render(request,'admin.html')

                    else:
                        print("Password is already taken")
                        return render(request,'signup.html')
                        
                else:
                    print("Email is already registered")
                    return render(request,'signup.html')
                    
            else:
                print("Number is already registered")
                return render(request,'signup.html')
                        
        else:
            print("You cannot register, this app is only for JCOET College")
            return render(request,'signup.html')

    return render(request,'signup.html')


        

            
                
                
                

                    

def teamPage(request):
    return render(request,'team.html')