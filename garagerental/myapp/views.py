from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import RegistrationForm
# , VehicleOwnForm, LoginForm, GarageOwnForm, GarageForm, VehicleForm, RentalForm, ReviewsForm
# from .models import User, Garage, Reviews, Vehicle, VehicleOwner, GarageOwner, Rentals
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import date

# Create your views here.
def LandingPage(request):
    return render(request, 'Homepage/LandingPage.html')

class RegistrationView(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request, 'Homepage/register.html' , {'form':form})

def HomePage(request):
    return render(request, 'Homepage/home.html')

def mygarage(request):
    return render(request, 'Homepage/mygarage.html')

def myvehicle(request):
    return render(request, 'Homepage/myvehicle.html')

def myrent(request):
    return render(request, 'Homepage/myrent.html')

def myreviews(request):
    return render(request, 'Homepage/myreviews.html')

def search_view(request):
    return render(request,'Homepage/garagelist.html')

def ProfilePage(request):
    return render(request, 'Homepage/profile.html',{'active':'btn-warning'})
