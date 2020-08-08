import datetime

from django.shortcuts import render

from . import forms
from .models import *
from .statcovid import *


# Home
def home(request):
    res = get_stats('russia', 'moscow')
    return render(request, 'index.html', {'f0': res['0'],'f1': res['1'],'f2': res['2'],'f3': res['3'],'f4': res['4'],'f5': res['5'],'f6': res['6'],'f7': res['7'],'f8': res['8']})


# User
def signup(request):
    form = forms.PatientSignupForm(request.POST or None)

    if form.is_valid():
        patient = form.save()

    return render(request, 'signup.html', {'form': form})


# Vaccination
def vaccination(request):
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
