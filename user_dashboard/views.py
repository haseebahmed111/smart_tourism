from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url="/account/login/")
def dashboard(request):
    return render(request, 'user_dashboard/index.html')


@login_required(login_url="/account/login/")
def share_trip_data(request):
    return render(request, 'user_dashboard/share_trip_data.html')
