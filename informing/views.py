from django.shortcuts import render
from . import forms


# Home
def home(request):
    return render(request, 'index.html', {})


# User
def signup(request):
    form = forms.PatientSignupForm(request.POST or None)

    if form.is_valid():
        patient = form.save()

    return render(request, 'signup.html', {'form': form})
