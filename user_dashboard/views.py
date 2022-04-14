from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ShareTripForm, RoleForm
from .models import ShareTrip


# Create your views here.
# @login_required(login_url="/account/login/")
def dashboard(request):
    shared_tips = ShareTrip.objects.filter(user=request.user)
    return render(request, 'user_dashboard/index.html', {'shared_trips': shared_tips})


@login_required(login_url="/account/login/")
def share_trip_data(request):
    if request.method == "POST":
        form = ShareTripForm(request.POST, request.FILES)
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


@login_required(login_url="/account/login/")
def update_trip_data(request, id):
    shared_data = ShareTrip.objects.get(id=id)
    form = ShareTripForm(instance=shared_data)
    if request.method == "POST":
        form = ShareTripForm(request.POST, request.FILES)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            return redirect('dashboard')
        else:
            print(form.errors)
            msg = 'Form is not valid'
    return render(request, 'user_dashboard/share_trip_data.html', {'form': form})


@login_required(login_url="/account/login/")
def delete_trip_data(request, id):
    shared_data = ShareTrip.objects.get(id=id)
    return render(request, 'user_dashboard/delete_trip.html', {'shared_data': shared_data})


@login_required(login_url="/account/login/")
def delete_trip_data_check(request, id, check):
    shared_data = ShareTrip.objects.get(id=id)
    if check:
        shared_data.delete()
    return redirect('dashboard')


@login_required(login_url="/account/login/")
def role_elevation(request):
    is_requested = False
    if request.method == "POST":
        form = RoleForm(request.POST, request.FILES)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            is_requested = True
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:
        form = RoleForm()
    return render(request, 'user_dashboard/request_elevation.html', {'form': form, 'is_requested': is_requested})


@login_required(login_url="/account/login/")
def complaint(request):
    is_requested = False
    if request.method == "POST":
        form = RoleForm(request.POST, request.FILES)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            is_requested = True
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:
        form = RoleForm()
    return render(request, 'user_dashboard/request_elevation.html', {'form': form, 'is_requested': is_requested})
