from django.shortcuts import render, redirect
from .forms import SignInForm
from .models import One

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = One.objects.get(username=username, password=password)
                # Handle successful sign-in, for example, set session variables, redirect, etc.
                # For now, let's just print a message.
                print("Signin successful!")
            except One.DoesNotExist:
                # Handle invalid credentials, for example, display an error message, redirect, etc.
                # For now, let's just print a message.
                print("Invalid credentials")
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})

def signup(request):
    return render(request, 'signup.html')

def otp(request):
    return render(request, 'otp.html')

def employerprofile(request):
    return render(request, 'employerprofile.html')

def profileform(request):
    return render(request, 'profileform.html')

def edit(request):
    return render(request, 'edit.html')

def hodprofile(request):
    return render(request, 'hodprofile.html')

def employeenmbr(request):
    return render(request, 'employeenmbr.html')

def addemployee(request):
    return render(request, 'addemployee.html')

def mainrepresentative(request):
    return render(request, 'mainrepresentative.html')

def profileinfo(request):
    return render(request, 'profileinfo.html')

def companydashboard(request):
    return render(request, 'companydashboard.html')

def table(request):
    return render(request, 'table.html')

def notifications(request):
    return render(request, 'notifications.html')

def maindashboard(request):
    return render(request, 'maindashboard.html')

def departments(request):
    return render(request, 'departments.html')

def projects(request):
    return render(request, 'projects.html')

def admindashboard(request):
     return render(request, 'admindashboard.html')

def base(request):
    return render(request, 'base.html')

    














