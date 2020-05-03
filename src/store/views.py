import requests
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .forms import CreateUserForm
from .forms import Profileform

#home view
def home(request):
    return render(request, 'index.html')


def Aboutus(request):
    return render(request, 'about.html')
#UserLogin
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'index.html', context)


#Registration page
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, "my-account.html", context)


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def dashboard_messages(request):
    return render(request, 'dashboard-messages.html')

def dashboard_bookings(request):
    return render(request, 'dashboard-bookings.html')

def dashboard_wallet(request):
    return render(request, 'dashboard-wallet.html')

def dashboard_listing(request):
    return render(request, 'dashboard-my-listings.html')

def dashboard_reviews(request):
    return render(request, 'dashboard-reviews.html')

def dashboard_bookmarks(request):
    return render(request, 'dashboard-bookmarks.html')

def dashboardAddlist(request):
    return render(request, 'dashboard-add-listing.html')

def dashboard_profile(request):
    return render(request, 'dashboard-my-profile.html')


def profile(request):
    form = Profileform()
    if request.method == 'POST':
        form = Profileform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, "dashboard-my-profile.html", context)