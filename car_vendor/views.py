from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CarVendorProfileFrom,CarForm

# Create your views here.
from car_vendor.models import Car, CarVendorProfile


@login_required(login_url="/login/")
def index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'car_vendor/index.html',{'cars':cars})

@login_required(login_url="/login/")
def add_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            return redirect('car_vendor_home')
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:
        form = CarForm()
    return render(request, 'car_vendor/add_car.html',{'form':form})

@login_required(login_url="/login/")
def delete_car(request,id):
    car = Car.objects.get(id=id)
    return render(request, 'car_vendor/delete_car.html',{'car':car})

@login_required(login_url="/login/")
def delete_car_check(request,id,check):
    car = Car.objects.get(id=id)
    if check:
        car.delete()
        return redirect('car_vendor_home')
    return render(request, 'car_vendor/delete_car.html',{'car':car})


@login_required(login_url="/login/")
def update_car(request,id):
    car = Car.objects.get(id=id)
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES,instance=car)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            return redirect('car_vendor_home')
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:
        form = CarForm(instance=car)
    return render(request, 'car_vendor/add_car.html',{'form':form})

@login_required(login_url="/login/")
def car_vendor_profile(request):
    try:
        profile = CarVendorProfile.objects.get(user=request.user)
    except CarVendorProfile.DoesNotExist:
        profile = None
    if request.method == "POST":
        form = CarVendorProfileFrom(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            return redirect('car_vendor_home')
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:

        form = CarVendorProfileFrom(instance=profile)
    return render(request, 'car_vendor/car_vendor_profile.html',{'form':form})
