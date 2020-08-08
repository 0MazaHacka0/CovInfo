from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.shortcuts import render, redirect
import datetime

from django.shortcuts import render

from CovInfo import settings
from . import forms
from .models import *
from .statcovid import *


# Home
def home(request):
    do_every_midnight()
    res = get_stats('russia', 'voronezh')
    return render(request, 'index.html',
                  {'f0': res['0'], 'f1': res['1'], 'f2': res['2'], 'f3': res['3'], 'f4': res['4'], 'f5': res['5'],
                   'f6': res['6'], 'f7': res['7'], 'f8': res['8']})


# Account
def account(request):
    if request.user.is_anonymous:
        return render(request, 'login.html', {})
    return render(request, 'account.html', {})


# User
# Login
def login(request):
    if request.method == "GET":
        return render(request, 'login.html', {})
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is None or user.is_anonymous:
            return render(request, 'login.html', {'message': 'Неправильный логин или пароль!'})
        else:
            return render(request, 'account.html', {})


# Signup
def signup(request):
    form = forms.PatientSignupForm(request.POST or None)
    if form.is_valid():
        patient = form.save()
    if request.method == "GET":
        return render(request, 'signup.html', {'form': form})
    else:
        return render(request, 'login.html', {})


# Logout
def logout(request):
    return render(request, 'index.html', {})


# from celery import task
# from celery.decorators import periodic_task
# from celery.task.schedules import crontab
# from celery.utils.log import get_task_logger
# @periodic_task(run_every=crontab(minute="0", hour=""))
def do_every_midnight():
    l = []
    [l.append(i.email) for i in list(Patient.objects.all())]
    send_mail('Тема', 'Тело письма', "srv.ru", l)


# Vaccination.
def vaccination(request):
    if request.user.is_anonymous:
        return render(request, 'login.html', {})
    if request.method == "GET":
        return render(request, 'vaccination.html', {})
    else:
        user = request.user
        hospital = Hospital()
        hospital.name = request.POST.get("center")
        hospital.date = request.POST.get("date")
        hospital.status = 'vaccination'
        hospital.patient = user
        hospital.save()
        hospital = Hospital()
        hospital.name = request.POST.get("center")
        hospital.date = request.POST.get("date") + datetime.timedelta(days=15)
        hospital.status = 're-vaccination'
        hospital.patient = user
        hospital.save()
    return render(request, 'index.html', {})
