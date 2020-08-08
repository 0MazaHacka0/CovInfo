from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import Patient


class PatientSignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        """
        Disable password check

        :param args:
        :param kwargs:
        """
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    first_name = forms.CharField()
    last_name = forms.CharField()
    passport_number = forms.NumberInput()
    passport_serial = forms.NumberInput()
    address = forms.CharField()
    email = forms.EmailInput()
    phone = forms.CharField()

    class Meta(UserCreationForm):
        model = Patient
        fields = ('email',)


class VaccinationForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(VaccinationForm, self).__init__(*args, **kwargs)

    hospital = forms.CharField()
    date = forms.DateField()
    omc = forms.CharField()
