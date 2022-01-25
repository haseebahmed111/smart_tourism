from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from user_dashboard.models import ShareTrip


def index(request):
    shared_trips = ShareTrip.objects.all()
    return render(request, 'home/examples/get_recommendations.html', {'shared_trips': shared_trips})


def login(request):
    return render(request, 'home/examples/login-page.html')


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


def share_data(request):
    return render(request, 'home/examples/share_your_trip_data.html')


def signup(request):
    return render(request, 'home/examples/signup-page.html')
