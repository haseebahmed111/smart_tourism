from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render


# Create your views here.
@login_required(login_url="/account/login/")
def index(request):
    users = User.objects.all().exclude(username=request.user.username)
    users_data = []
    for user in users:
        groups = Group.objects.filter(user=user)
        print(groups)
        users_data.append([user, groups])

    return render(request, 'management/index.html', {'users': users_data})


@login_required(login_url="/account/login/")
def add_car_vendor(request):
    return render(request, 'management/add_car_vendor.html')


@login_required(login_url="/account/login/")
def add_trip_vendor(request):
    return render(request, 'management/add_trip_vendor.html')


@login_required(login_url="/account/login/")
def add_tour_guide(request):
    return render(request, 'management/add_tour_guide.html')


@login_required(login_url="/account/login/")
def update_user(request):
    return render(request, 'management/update_user.html')


@login_required(login_url="/account/login/")
def delete_user(request):
    return render(request, 'management/delete_user.html')
