from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from trip_vendor.forms import TripVendorProfileFrom, TripForm
from trip_vendor.models import TripVendorProfile, Trip


@login_required(login_url="/account/login/")
def index(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'trip_vendor/index.html', {'trips': trips})


@login_required(login_url="/account/login/")
def add_trip(request):
    if request.method == "POST":
        form = TripForm(request.POST, request.FILES)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            return redirect('trip_vendor_home')
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:
        form = TripForm()
    return render(request, 'trip_vendor/add_trip.html', {'form': form})


@login_required(login_url="/account/login/")
def delete_trip(request, id):
    trip = Trip.objects.get(id=id)

    return render(request, 'trip_vendor/delete_trip.html', {'trip': trip})


@login_required(login_url="/account/login/")
def delete_trip_check(request, id, check):
    trip = Trip.objects.get(id=id)
    if check:
        trip.delete()
        return redirect('trip_vendor_home')
    return render(request, 'trip_vendor/delete_trip.html', {'trip': trip})


@login_required(login_url="/account/login/")
def update_trip(request, id):
    trip = Trip.objects.get(id=id)
    if request.method == "POST":
        form = TripForm(request.POST, request.FILES, instance=trip)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            return redirect('trip_vendor_home')
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:
        form = TripForm(instance=trip)
    return render(request, 'trip_vendor/add_trip.html', {'form': form})


@login_required(login_url="/account/login/")
def trip_vendor_profile(request):
    try:
        profile = TripVendorProfile.objects.get(user=request.user)
    except TripVendorProfile.DoesNotExist:
        profile = None
    if request.method == "POST":
        form = TripVendorProfileFrom(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            return redirect('trip_vendor_home')
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:

        form = TripVendorProfileFrom(instance=profile)
    return render(request, 'trip_vendor/trip_vendor_profile.html', {'form': form})
