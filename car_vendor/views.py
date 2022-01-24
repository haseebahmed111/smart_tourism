from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return render(request, 'car_vendor/index.html')

@login_required(login_url="/login/")
def add_car(request):
    return render(request, 'car_vendor/add_car.html')

@login_required(login_url="/login/")
def delete_car(request):
    return render(request, 'car_vendor/delete_car.html')

@login_required(login_url="/login/")
def update_car(request):
    return render(request, 'car_vendor/update_car.html')

@login_required(login_url="/login/")
def car_vendor_profile(request):
    return render(request, 'car_vendor/car_vendor_profile.html')
