from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.home.models import CustomTripOffer
from management.views import allow_access
from .forms import ShareTripForm, RoleForm, ComplaintForm
from .models import ShareTrip


@login_required(login_url="/account/login/")
def dashboard(request):
    access_level = allow_access(request)
    if not access_level:
        return redirect('role_elevation')
    shared_tips = ShareTrip.objects.filter(user=request.user)
    return render(request, 'user_dashboard/index.html', {'shared_trips': shared_tips, 'access_level': access_level})


@login_required(login_url="/account/login/")
def share_trip_data(request):
    access_level = allow_access(request)
    if not access_level:
        return redirect('role_elevation')
    if request.method == "POST":
        form = ShareTripForm(request.POST, request.FILES)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            return redirect('view_shared_trip', shared_data.id)
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:
        form = ShareTripForm()
    return render(request, 'user_dashboard/share_trip_data.html', {'form': form, 'access_level': access_level})


@login_required(login_url="/account/login/")
def update_trip_data(request, id):
    access_level = allow_access(request)
    if not access_level:
        return redirect('role_elevation')
    shared_data = ShareTrip.objects.get(id=id)
    if request.method == "POST":
        form = ShareTripForm(request.POST, request.FILES, instance=shared_data)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            return redirect('dashboard')
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:
        form = ShareTripForm(instance=shared_data)

    return render(request, 'user_dashboard/share_trip_data.html', {'form': form, 'access_level': access_level})


@login_required(login_url="/account/login/")
def delete_trip_data(request, id):
    access_level = allow_access(request)
    if not access_level:
        return redirect('role_elevation')
    shared_data = ShareTrip.objects.get(id=id)
    return render(request, 'user_dashboard/delete_trip.html',
                  {'shared_data': shared_data, 'access_level': access_level})


@login_required(login_url="/account/login/")
def delete_trip_data_check(request, id, check):
    access_level = allow_access(request)
    if not access_level:
        return redirect('role_elevation')
    shared_data = ShareTrip.objects.get(id=id)
    if check:
        shared_data.delete()
    return redirect('dashboard')


@login_required(login_url="/account/login/")
def role_elevation(request):
    access_level = allow_access(request)
    if not access_level:
        return redirect('role_elevation')
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
    return render(request, 'user_dashboard/request_elevation.html',
                  {'form': form, 'is_requested': is_requested, 'access_level': access_level})


@login_required(login_url="/account/login/")
def complaint(request):
    access_level = allow_access(request)
    if not access_level:
        return redirect('role_elevation')
    is_complain_registered = False
    if request.method == "POST":
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            is_complain_registered = True
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:
        form = ComplaintForm()
    return render(request, 'user_dashboard/register_complaint.html',
                  {'form': form, 'is_complain_registered': is_complain_registered, 'access_level': access_level})


@login_required(login_url="/account/login/")
def view_custom_offers(request):
    access_level = allow_access(request)
    custom_offers = CustomTripOffer.objects.filter(user=request.user)
    ctx = {
        'custom_offers': custom_offers,
        'access_level': access_level
    }
    return render(request, 'user_dashboard/custom_trip_offers.html', ctx)
