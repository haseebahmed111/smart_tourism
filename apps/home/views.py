import math
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from apps.authentication.forms import SignUpFormHome, LoginForm
from apps.home.forms import RecommendationForm, CustomTripOfferForm, CustomTripOfferViewForm, CustomTripOfferBidForm
from apps.home.models import City, CustomTripOffer, CustomTripBid
from car_vendor.models import Car, CarVendorProfile
from management.models import WebsiteSettings
from management.views import allow_access
from tour_guide.models import TourGuideProfile, Language
from trip_vendor.models import Trip, TripVendorProfile
from user_dashboard.forms import SharedTripImageForm, SharedTripVideoLinkForm
from user_dashboard.models import ShareTrip, SharedTripImage, SharedTripVideoLink


def index(request):
    access_level = allow_access(request)
    form = RecommendationForm(request.POST or None)
    results = False
    if request.method == "POST":
        if form.is_valid():
            results = True
            from_city = form.cleaned_data.get('starting_location')
            province = form.cleaned_data.get('province')
            area = form.cleaned_data.get('area')
            city_to_visit = form.cleaned_data.get('city')
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

            cities_results = list(set(cities))

            # Collecting Cars from Vendor Cars
            tour_guides_results = TourGuideProfile.objects.filter(city__in=cities)

            print(province, area, city_to_visit)

            print("\n\n0")

            shared_trips = []
            vendor_trips = []
            vendor_cars = []
            tour_guides = []
            cities = []
            if province:
                print("Province filter:", province)

                for trip in shared_trips_results:
                    if trip.to_city.province == province:
                        shared_trips.append(trip)
                for trip in vendor_trips_results:
                    if trip.trip_from.province == province:
                        vendor_trips.append(trip)
                for car in vendor_cars_results:
                    if car.city.province == province:
                        vendor_cars.append(car)
                for guide in tour_guides_results:
                    if guide.city.province == province:
                        tour_guides.append(guide)
                for city in cities_results:
                    if city.province == province:
                        cities.append(city)

                shared_trips_results = shared_trips
                vendor_trips_results = vendor_trips
                vendor_cars_results = vendor_cars
                tour_guides_results = tour_guides
                cities_results = cities

            shared_trips = []
            vendor_trips = []
            vendor_cars = []
            tour_guides = []
            cities = []
            if area:
                print("Area filter:", area)

                for trip in shared_trips_results:
                    if trip.to_city.area == area:
                        shared_trips.append(trip)
                for trip in vendor_trips_results:
                    if trip.trip_from.area == area:
                        vendor_trips.append(trip)
                for car in vendor_cars_results:
                    if car.city.area == area:
                        vendor_cars.append(car)
                for guide in tour_guides_results:
                    if guide.city.area == area:
                        tour_guides.append(guide)
                for city in cities_results:
                    if city.area == area:
                        cities.append(city)

                shared_trips_results = shared_trips
                vendor_trips_results = vendor_trips
                vendor_cars_results = vendor_cars
                tour_guides_results = tour_guides
                cities_results = cities

            shared_trips = []
            vendor_trips = []
            vendor_cars = []
            tour_guides = []
            cities = []

            if city_to_visit:
                print("City filter:", city_to_visit)

                for trip in shared_trips_results:
                    if trip.to_city.name == city_to_visit:
                        shared_trips.append(trip)
                for trip in vendor_trips_results:
                    if trip.trip_from.name == city_to_visit:
                        vendor_trips.append(trip)
                for car in vendor_cars_results:
                    if car.city.name == city_to_visit:
                        vendor_cars.append(car)
                for guide in tour_guides_results:
                    if guide.city.name == city_to_visit:
                        tour_guides.append(guide)
                for city_ in cities_results:
                    if city_.name == city_to_visit:
                        cities.append(city_)

                shared_trips_results = shared_trips
                vendor_trips_results = vendor_trips
                vendor_cars_results = vendor_cars
                tour_guides_results = tour_guides
                cities_results = cities

            ctx = {
                'shared_trips': shared_trips_results,
                'vendor_trips': vendor_trips_results,
                'vendor_cars': vendor_cars_results,
                'tour_guides': tour_guides_results,
                'cities': cities_results,
                'form': form,
                'results': results,
                'access_level': access_level,

            }
            return render(request, 'home/examples/get_recommendations.html', ctx)
        else:
            print(form.errors)

    try:
        settings = WebsiteSettings.objects.last()
        if not settings:
            settings = WebsiteSettings.objects.create()
            settings.save()

    except:
        settings = WebsiteSettings.objects.create()
        settings.save()

    shared_trips = ShareTrip.objects.all().order_by('shared_on')[:settings.number_of_objects][::-1]
    vendor_trips = Trip.objects.all().order_by('created')[:settings.number_of_objects][::-1]
    vendor_cars = Car.objects.all().order_by('created')[:settings.number_of_objects][::-1]
    tour_guides = TourGuideProfile.objects.all().order_by('information_added_on')[:settings.number_of_objects][::-1]
    cities = None

    ctx = {
        'shared_trips': shared_trips,
        'vendor_trips': vendor_trips,
        'vendor_cars': vendor_cars,
        'tour_guides': tour_guides,
        'cities': cities,
        'form': form,
        'results': results,
        'access_level': access_level,

    }
    return render(request, 'home/examples/get_recommendations.html', ctx)


def view_trip(request, id):
    access_level = allow_access(request)
    trip = Trip.objects.get(id=id)
    is_author = False
    if request.user.is_authenticated and request.user == trip.user:
        is_author = True
        # if request.method == "POST":
        #     form = TripImageForm(request.POST, request.FILES)
        #     if form.is_valid():
        #         image = form.save(commit=False)
        #         image.trip = trip
        #         image.save()
        #         return redirect('view_trip', trip.id)
        # else:
        #     form = TripImageForm()

    ctx = {
        'trip': trip,
        'access_level': access_level,
        'is_author': is_author
    }
    return render(request, 'home/examples/trip_page.html', ctx)


def view_car(request, id):
    access_level = allow_access(request)
    car = Car.objects.get(id=id)
    is_author = False
    if request.user.is_authenticated and request.user == car.user:
        is_author = True
        # if request.method == "POST":
        #     form = TripImageForm(request.POST, request.FILES)
        #     if form.is_valid():
        #         image = form.save(commit=False)
        #         image.trip = trip
        #         image.save()
        #         return redirect('view_trip', trip.id)
        # else:
        #     form = TripImageForm()

    ctx = {
        'car': car,
        'access_level': access_level,
        'is_author': is_author
    }
    return render(request, 'home/examples/car_page.html', ctx)


def view_shared_trip(request, id):
    trip = ShareTrip.objects.get(id=id)
    trip_images = SharedTripImage.objects.filter(trip__id=trip.id)
    video_links = SharedTripVideoLink.objects.filter(trip__id=trip.id)
    is_author = False
    form1 = None
    form2 = None
    if request.user.is_authenticated and request.user == trip.user:
        is_author = True
        if request.method == "POST":
            form1 = SharedTripImageForm(request.POST, request.FILES, prefix="form1")
            form2 = SharedTripVideoLinkForm(request.POST, prefix="form2")
            if form1.is_valid():
                image = form1.save(commit=False)
                image.trip = trip
                image.save()
                return redirect('view_shared_trip', trip.id)
            if form2.is_valid():
                link = form2.save(commit=False)
                link.trip = trip
                link.save()
                return redirect('view_shared_trip', trip.id)
        else:
            form1 = SharedTripImageForm(prefix="form1")
            form2 = SharedTripVideoLinkForm(prefix="form2")

    ctx = {
        'trip': trip,
        'trip_images': trip_images,
        'video_links': video_links,
        'is_author': is_author,
        'form1': form1,
        'form2': form2,
    }
    return render(request, 'home/examples/shared_trip_page.html', ctx)


@login_required(login_url="/account/login/")
def delete_shared_trip_image(request, trip_id, id):
    trip_image = SharedTripImage.objects.get(id=id)
    if request.user == trip_image.trip.user:
        trip_image.delete()
    return redirect('view_shared_trip', trip_id)


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
                if request.GET.get('next', '/'):
                    return redirect(request.GET.get('next', '/'))
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

    return render(request, 'home/examples/login-page.html', {'form': form, 'msg': msg})


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


@login_required(login_url="/login/")
def view_tour_guide_profile(request, id):
    access_level = allow_access(request)
    guide = TourGuideProfile.objects.get(id=id)
    languages = Language.objects.filter(user=guide.user)
    is_author = False
    if request.user.is_authenticated and request.user == guide.user:
        is_author = True
        # if request.method == "POST":
        #     form = TripImageForm(request.POST, request.FILES)
        #     if form.is_valid():
        #         image = form.save(commit=False)
        #         image.trip = trip
        #         image.save()
        #         return redirect('view_trip', trip.id)
        # else:
        #     form = TripImageForm()

    ctx = {
        'guide': guide,
        'languages': languages,
        'access_level': access_level,
        'is_author': is_author,
    }
    return render(request, 'home/examples/tourguide_profile.html', ctx)


@login_required(login_url="/login/")
def view_trip_vendor_profile(request, id):
    access_level = allow_access(request)
    vendor = TripVendorProfile.objects.get(id=id)
    trips = Trip.objects.filter(vendor=vendor)
    is_author = False
    if request.user.is_authenticated and request.user == vendor.user:
        is_author = True
        # if request.method == "POST":
        #     form = TripImageForm(request.POST, request.FILES)
        #     if form.is_valid():
        #         image = form.save(commit=False)
        #         image.trip = trip
        #         image.save()
        #         return redirect('view_trip', trip.id)
        # else:
        #     form = TripImageForm()

    ctx = {
        'vendor': vendor,
        'trips': trips,
        'access_level': access_level,
        'is_author': is_author,
    }
    return render(request, 'home/examples/trip_vendor_profile.html', ctx)


@login_required(login_url="/login/")
def view_car_vendor_profile(request, id):
    access_level = allow_access(request)
    vendor = CarVendorProfile.objects.get(id=id)
    cars = Car.objects.filter(vendor=vendor)
    is_author = False
    if request.user.is_authenticated and request.user == vendor.user:
        is_author = True
        # if request.method == "POST":
        #     form = TripImageForm(request.POST, request.FILES)
        #     if form.is_valid():
        #         image = form.save(commit=False)
        #         image.trip = trip
        #         image.save()
        #         return redirect('view_trip', trip.id)
        # else:
        #     form = TripImageForm()

    ctx = {
        'vendor': vendor,
        'cars': cars,
        'access_level': access_level,
        'is_author': is_author,
    }
    return render(request, 'home/examples/car_vendor_profile.html', ctx)


@login_required(login_url="/login/")
def create_private_trip(request):
    access_level = allow_access(request)
    form = CustomTripOfferForm(None or request.POST)
    if request.method == "POST":
        if form.is_valid():
            last_offer = CustomTripOffer.objects.filter(user=request.user)
            if not last_offer.exists() or last_offer.latest('created').created < timezone.now() - timezone.timedelta(
                    days=7):
                custom_trip = form.save(commit=False)
                custom_trip.user = request.user
                custom_trip.save()
                return redirect('view_private_trip', custom_trip.id)

    ctx = {
        # 'vendor': vendor,
        # 'cars': cars,
        'access_level': access_level,
        'form': form,
        # 'is_author': is_author,
    }
    return render(request, 'home/examples/Private_trip_offer.html', ctx)


@login_required(login_url="/login/")
def view_private_trip(request, id):
    access_level = allow_access(request)
    offer = CustomTripOffer.objects.get(id=id)
    form = CustomTripOfferViewForm(instance=offer, prefix='form1')
    post = True
    form2 = None
    is_author = False
    previous_bids = None

    if request.user == offer.user:
        is_author = True
        previous_bids = CustomTripBid.objects.filter(offer=offer)
    elif access_level['trip_vendor']:
        previous_bids = CustomTripBid.objects.filter(user=request.user,offer=offer)
        try:
            profile = TripVendorProfile.objects.get(user=request.user)
        except TripVendorProfile.DoesNotExist:
            return redirect('trip_vendor_profile')
        form2 = CustomTripOfferBidForm(None or request.POST, prefix='form2')
        if request.method == 'POST':
            if form2.is_valid():
                bid = form2.save(commit=False)
                bid.user = request.user
                bid.offer = offer
                bid.save()


    ctx = {
        'access_level': access_level,
        'form': form,
        'form2': form2,
        'post': post,
        'is_author': is_author,
        'previous_bids': previous_bids,
    }
    return render(request, 'home/examples/Private_trip_offer.html', ctx)


def detect_trip_vendor(request,id):
    vendor = TripVendorProfile.objects.get(user__id=id)
    return redirect('view_trip_vendor_profile',vendor.id)


# def car_vendor(request):
#     return render(request, 'home/examples/car_vendor_profile.html')
#
#
# def tour_guide(request):
#     return render(request, 'home/examples/tourguide_profile.html')
#
#
# def vendor(request):
#     return render(request, 'home/examples/vendor_profile.html')
#
#

#
# def update_trip(request):
#     return render(request, 'home/examples/update_trip_data.html')
#
#
# def search(request):
#     return render(request, 'home/examples/search_trips.html')
#
#
# def search(request, text):
#     print(text)
#     return render(request, 'home/examples/search_trips.html')
#
#
# def share_data(request):
#     return render(request, 'home/examples/share_your_trip_data.html')
