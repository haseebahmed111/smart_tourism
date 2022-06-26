from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect


# Create your views here.
@login_required(login_url="/account/login/")
def index(request):
    access_level = allow_access(request, ['management'])
    if not access_level:
        return redirect('role_elevation')
    return redirect('admin:index')
    users = User.objects.all().exclude(username=request.user.username)
    users_data = []
    for user in users:
        groups = Group.objects.filter(user=user)
        print(groups)
        users_data.append([user, groups])

    return render(request, 'management/index.html', {'users': users_data, 'access_level': access_level})


@login_required(login_url="/account/login/")
def add_car_vendor(request):
    access_level = allow_access(request, ['management'])
    if not access_level:
        return redirect('role_elevation')
    return render(request, 'management/add_car_vendor.html',{'access_level': access_level})


@login_required(login_url="/account/login/")
def add_trip_vendor(request):
    access_level = allow_access(request, ['management'])
    if not access_level:
        return redirect('role_elevation')
    return render(request, 'management/add_trip_vendor.html',{'access_level': access_level})


@login_required(login_url="/account/login/")
def add_tour_guide(request):
    access_level = allow_access(request, ['management'])
    if not access_level:
        return redirect('role_elevation')
    return render(request, 'management/add_tour_guide.html',{'access_level': access_level})


@login_required(login_url="/account/login/")
def update_user(request):
    access_level = allow_access(request, ['management'])
    if not access_level:
        return redirect('role_elevation')
    return render(request, 'management/update_user.html',{'access_level': access_level})


@login_required(login_url="/account/login/")
def delete_user(request):
    access_level = allow_access(request, ['management'])
    if not access_level:
        return redirect('role_elevation')
    return render(request, 'management/delete_user.html',{'access_level': access_level})


def allow_access(request, allowed_groups=None):
    try:
        group = Group.objects.get(name='management')
    except:
        group = Group.objects.create(name='management')
        group.save()
    try:
        group = Group.objects.get(name='tour_guide')
    except:
        group = Group.objects.create(name='tour_guide')
        group.save()
    try:
        group = Group.objects.get(name='trip_vendor')
    except:
        group = Group.objects.create(name='trip_vendor')
        group.save()
    try:
        group = Group.objects.get(name='car_vendor')
    except:
        group = Group.objects.create(name='car_vendor')
        group.save()

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
    groups = request.user.groups.all()
    for group in groups:
        evaluation_results[group.name] = True
    if not allowed_groups or len(allowed_groups) < 1:
        return evaluation_results
    if request.user.groups.filter(name__in=allowed_groups).exists():
        return evaluation_results
    else:
        return False
