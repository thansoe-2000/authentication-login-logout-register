from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.contrib import messages

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'registration/dashboard.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
    
        context = {
            'form':form,
        }
        return render(request, 'registration/register.html', context)
        
    

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'registration/login.html', context)
        

def logoutPage(request):
    logout(request)
    return redirect('login')