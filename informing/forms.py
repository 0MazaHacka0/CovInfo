from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import Patient


class PatientSignupForm(UserCreationForm):

    name = forms.CharField()
    surname = forms.CharField()
    passport_number = forms.NumberInput()
    passport_serial = forms.NumberInput()
    address = forms.CharField()
    email = forms.EmailInput()
    phone = forms.CharField()

    class Meta(UserCreationForm):
        model = Patient
        fields = ('email',)
