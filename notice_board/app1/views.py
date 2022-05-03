from django.shortcuts import render


# Create your views here.

def learn(request):
    data={
        'title':'web',
        'student':[
            {'name':'jivan', 'mo':'9922966708'},
            {'name':'jivan', 'mo':'9373514483'},
            {'name':'jp', 'mo':'9843514483'}
        ],
        'notice':['it is hereby inform that','our college is going to','organize one day fun day']

    }
    return render(request, 'app.html',data)
