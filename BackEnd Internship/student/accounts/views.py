from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User , auth


# Create your views here.

def accounts(requests):
    return render(requests,'accounts.html')


def login(requests):
    if requests.method == 'POST':
        username = requests.POST['username']
        password = requests.POST['password']

        user=auth.authenticate(
            username=username,
            password=password
        )

        if user is not None:
            auth.login(requests,user)
            print('login successful')
            return redirect('/')
    else:
        print('error')
        
    return render(requests,'loginAcc.html')


def signup(requests):
    if requests.method == 'POST':
        username = requests.POST['username']
        fname = requests.POST['fname']
        lname = requests.POST['lname']
        email = requests.POST['email']
        password = requests.POST['password']
        user = User.objects.create_user(
        username = username,
        first_name = fname,
        last_name = lname,
        email = email,
        password = password 
        )
        print('user created')
        return redirect('/')
    else:
        print('error')
    return render(requests,'signupAcc.html')