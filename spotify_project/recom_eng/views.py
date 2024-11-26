from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import SignUpForm, LoginForm

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                # Check if the user exists
                user = User.objects.get(username=username)
                # Validate the password
                if user.password == password:
                    return redirect('dashboard')
                else:
                    messages.error(request, "Password is incorrect")  # Incorrect password
            except User.DoesNotExist:
                messages.error(request, "Invalid credentials")  # Username doesn't exist
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html', {'message': 'Your AI music recommendations will appear here!'})
