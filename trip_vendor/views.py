from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url="/account/login/")
def index(request):
    return render(request, 'trip_vendor/index.html')


@login_required(login_url="/account/login/")
def add_trip(request):
    return render(request, 'trip_vendor/add_trip.html')


@login_required(login_url="/account/login/")
def delete_trip(request):
    return render(request, 'trip_vendor/delete_trip.html')


@login_required(login_url="/account/login/")
def update_trip(request):
    return render(request, 'trip_vendor/update_trip.html')


@login_required(login_url="/account/login/")
def trip_vendor_profile(request):
    return render(request, 'trip_vendor/trip_vendor_profile.html')
