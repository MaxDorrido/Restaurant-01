from contextlib import redirect_stderr
from urllib import request
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username, password= password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else :
            messages.info(request, 'invalid request')
            return redirect('login')
    else:    
        return render(request, 'Sign_in.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        user= User.objects.create_user(username= username, password= password1, first_name= first_name, last_name =last_name)
        user.save()
        return redirect('/')
    else:    
        return render(request, 'Sign_up.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
