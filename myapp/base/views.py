from django.shortcuts import render,redirect,get_object_or_404
from .models import Doctors,Speciality
from django.utils.timezone import now
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.db import models
from django.http import HttpResponse
from dotenv import load_dotenv
import os
load_dotenv()
# Create your views here.
def home(request):
    return render(request,'base/home.html')

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST' :
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not Exists")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')
             

    return render(request, 'base/login.html')

def logoutUser(request):
    logout(request)
    return redirect('home')