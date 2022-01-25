from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ShareTripForm
from .models import ShareTrip


# Create your views here.
# @login_required(login_url="/account/login/")
def dashboard(request):
    shared_tips = ShareTrip.objects.all()
    return render(request, 'user_dashboard/index.html', {'shared_trips': shared_tips})


# @login_required(login_url="/account/login/")
def share_trip_data(request):
    if request.method == "POST":
        form = ShareTripForm(request.POST)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            return redirect('dashboard')
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:
        form = ShareTripForm()
    return render(request, 'user_dashboard/share_trip_data.html', {'form': form})


# @login_required(login_url="/account/login/")
def update_trip_data(request):
    return render(request, 'user_dashboard/share_trip_data.html')


# @login_required(login_url="/account/login/")
def delete_trip_data(request):
    return render(request, 'user_dashboard/delete_trip.html')
