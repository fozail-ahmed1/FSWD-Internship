from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(requests):
    # return HttpResponse(" <h1> Hello world </h1>")
    fname='adam smith'
    age=12
    return render(requests,'home.html',{'name':fname , 'age':age})

def login(requests):
    # return HttpResponse("login page")
    username = 'Adam123'
    email = 'abcd@gmail.com'
    return render(requests,'login.html', {'username':username, 'email':email})

def signup(requests):
    lname = 'smith'
    return render(requests,'signup.html',{'lname':lname})

def add(requests):
    var1= requests.POST['num1']
    var2= requests.POST['num2']
    res=int(var1) + int(var2)
    return render(requests,'add.html',{'result':res})
