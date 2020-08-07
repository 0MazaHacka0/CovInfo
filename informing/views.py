from django.shortcuts import render
from . import forms


# User
def signup(request):
    form = forms.PatientSignupForm(request.POST or None)

    if form.is_valid():
        patient = form.save()

    return render(request, 'signup.html', {'form': form})

    #
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #     username = form.cleaned_data.get('username')
    #     my_password = form.cleaned_data.get('password1')
    #     user = authenticate(username=username, password=my_password)
    #     login(request, user)
    #     return redirect('index')
    # else:
    #     form = UserCreationForm()
    #     return render(request, 'signup.html', {'form': form})
