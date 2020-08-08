from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from . import forms
from .models import *
import datetime


# Home
def home(request):
    return render(request, 'index.html', {})


# Account
def account(request):
    return render(request, 'account.html', {})


# User
# Login
def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = authenticate(username=email, password=password)
    if user is not None and user.is_active:
        return redirect('home')

    return render(request, 'login.html', {})


# Signup
def signup(request):
    form = forms.PatientSignupForm(request.POST or None)

    if form.is_valid():
        patient = form.save()

    return render(request, 'signup.html', {'form': form})


# Logout
def log_out(request):
    logout(request)
    return render(request, 'index.html', {})


# Vaccination
@login_required
def vaccination(request):
    if request.method == "GET":
        return render(request, 'vaccination.html', {})
    else:
        user = Patient.objects.get(user=request.user)
        hospital = Hospital()
        hospital.name = request.POST.get("hospital")
        hospital.date = request.POST.get("date")
        hospital.status = 'vaccination'
        hospital.patient = user
        hospital.save()
        hospital = Hospital()
        hospital.name = request.POST.get("hospital")
        hospital.date = request.POST.get("date") + datetime.timedelta(days=15)
        hospital.status = 're-vaccination'
        hospital.patient = user
        hospital.save()
    return render(request, 'index.html', {})
