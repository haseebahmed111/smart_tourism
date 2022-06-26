from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect


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


def allow_access(request, allowed_groups=None):
    evaluation_results = {
        'management': False,
        'tour_guide': False,
        'car_vendor': False,
        'trip_vendor': False,
        'admin': False,
        'staff': False,
        'user': False,
    }
    if not request.user.is_authenticated:
        return evaluation_results
    evaluation_results['user'] = True
    if request.user.is_superuser:
        evaluation_results['admin'] = True
    if request.user.is_staff:
        evaluation_results['staff'] = True
    if not allowed_groups or len(allowed_groups) < 1:
        return evaluation_results
    if request.user.groups.filter(name__in=allowed_groups).exists():

        return evaluation_results
    else:
        return redirect('role_elevation')
