import math

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.authentication.forms import SignUpFormHome, LoginForm
from apps.home.forms import RecommendationForm
from apps.home.models import City
from car_vendor.models import Car
from tour_guide.models import TourGuideProfile
from trip_vendor.models import Trip
from user_dashboard.models import ShareTrip


def index(request):
    form = RecommendationForm(request.POST or None)
    results = False
    if request.method == "POST":
        if form.is_valid():
            results = True
            from_city = form.cleaned_data.get('starting_location')
            province = form.cleaned_data.get('province')
            area = form.cleaned_data.get('area')
            city = form.cleaned_data.get('city')
            days = form.cleaned_data.get('days')
            budget = form.cleaned_data.get('budget')
            persons = form.cleaned_data.get('persons')
            cities = []

            # Collecting Cities from Shared Trip Data
            shared_trips = ShareTrip.objects.filter(from_city=from_city).order_by('shared_on')
            shared_trips_results = []
            for trip in shared_trips:
                if budget:
                    try:
                        cost_per_person_day = trip.total_budget_spent / (
                                int(1 if days is None else trip.trip_duration) * int(
                            1 if persons is None else trip.persons))
                        if cost_per_person_day * (
                                int(1 if days is None else days) * int(1 if persons is None else persons)) <= budget:
                            cities.append(trip.to_city)
                            shared_trips_results.append(trip)

                        # cost_per_day = 1
                        # cost_per_person = 1
                        # if days:
                        #     cost_per_day = trip.total_budget_spent / trip.trip_duration
                        # if persons:
                        #     cost_per_person = trip.total_budget_spent/trip.persons
                        #
                        # if (cost_per_person * persons) <= budget:
                        #     cities |= trip.to_city
                    except ZeroDivisionError:
                        cities.append(trip.to_city)
                        shared_trips_results.append(trip)

                else:
                    cities.append(trip.to_city)
                    shared_trips_results.append(trip)

            # Collecting Cities from Vendor Trips
            vendor_trips = Trip.objects.filter(trip_from=from_city).order_by('created')
            vendor_trips_results = []
            for trip in vendor_trips:
                if budget:
                    try:
                        cost_per_person_day = trip.trip_price_per_person / (
                            int(1 if days is None else trip.trip_duration))
                        if cost_per_person_day * (
                                int(1 if days is None else days) * int(1 if persons is None else persons)) <= budget:
                            cities.append(trip.trip_to)
                            vendor_trips_results.append(trip)
                    except ZeroDivisionError:
                        cities.append(trip.trip_to)
                        vendor_trips_results.append(trip)

                else:
                    cities.append(trip.trip_to)
                    vendor_trips_results.append(trip)

            # Collecting Cars from Vendor Cars
            vendor_cars = Car.objects.filter(city=from_city).order_by('created')
            vendor_cars_results = []
            for car in vendor_cars:
                if budget:
                    try:
                        no_of_cars = math.ceil(int(1 if persons is None else persons) / car.seating_capacity)
                        if car.rent_without_driver * (
                                int(1 if days is None else days) * int(1 if persons is None else no_of_cars)) <= budget:
                            vendor_cars_results.append(car)
                    except ZeroDivisionError:
                        vendor_cars_results.append(car)
                else:
                    vendor_cars_results.append(car)

            cities = list(set(cities))

            # Collecting Cars from Vendor Cars
            tour_guides_results = TourGuideProfile.objects.filter(city__in=cities)

            ctx = {
                'shared_trips': shared_trips_results,
                'vendor_trips': vendor_trips_results,
                'vendor_cars': vendor_cars_results,
                'tour_guides': tour_guides_results,
                'cities': cities,
                'form': form,
                'results': results,

            }
            return render(request, 'home/examples/get_recommendations.html', ctx)
        else:
            print(form.errors)

    shared_trips = ShareTrip.objects.all().order_by('shared_on')[:10][::-1]
    vendor_trips = Trip.objects.all().order_by('created')[:10][::-1]
    vendor_cars = Car.objects.all().order_by('created')[:10][::-1]
    tour_guides = TourGuideProfile.objects.all().order_by('information_added_on')[:10][::-1]
    cities = None

    ctx = {
        'shared_trips': shared_trips,
        'vendor_trips': vendor_trips,
        'vendor_cars': vendor_cars,
        'tour_guides': tour_guides,
        'cities': cities,
        'form': form,
        'results': results

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


def view_trip(request,id):
    return render(request,'home/examples/trip_page.html')