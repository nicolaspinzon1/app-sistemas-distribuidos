from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  
from django.contrib.auth import login, logout # crear la cookie 
def home(request):
    return render(request, "home.html")

@login_required
def signout(request):
    logout(request)
    return render(request,"home.html")