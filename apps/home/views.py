from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.authentication.forms import SignUpFormHome, LoginForm
from car_vendor.models import Car
from tour_guide.models import TourGuideProfile
from trip_vendor.models import Trip
from user_dashboard.models import ShareTrip


def index(request):
    shared_trips = ShareTrip.objects.all()
    vendor_trips = Trip.objects.all()
    vendor_cars = Car.objects.all()
    tour_guides = TourGuideProfile.objects.all()
    ctx = {
        'shared_trips': shared_trips,
        'vendor_trips': vendor_trips,
        'vendor_cars': vendor_cars,
        'tour_guides': tour_guides

    }
    return render(request, 'home/examples/get_recommendations.html', ctx)


def home_login(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.groups.filter(name="management") or user.is_superuser:
                    return redirect('admin:index')
                if user.groups.filter(name="tour_guide"):
                    return redirect('tour_guide_home')
                if user.groups.filter(name="car_vendor"):
                    return redirect('car_vendor_home')
                if user.groups.filter(name="trip_vendor"):
                    return redirect('trip_vendor_home')
                return redirect("dashboard")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, 'home/examples/login-page.html', {'form': form})


def car_vendor(request):
    return render(request, 'home/examples/car_vendor_profile.html')


def tour_guide(request):
    return render(request, 'home/examples/tourguide_profile.html')


def vendor(request):
    return render(request, 'home/examples/vendor_profile.html')


def private_trip(request):
    return render(request, 'home/examples/Private_trip_offer.html')


def update_trip(request):
    return render(request, 'home/examples/update_trip_data.html')


def search(request):
    return render(request, 'home/examples/search_trips.html')


def search(request, text):
    print(text)
    return render(request, 'home/examples/search_trips.html')


def share_data(request):
    return render(request, 'home/examples/share_your_trip_data.html')


def signup(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpFormHome(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            return redirect('home_login')

        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:
        form = SignUpFormHome()
    return render(request, 'home/examples/signup-page.html', {'form': form})
