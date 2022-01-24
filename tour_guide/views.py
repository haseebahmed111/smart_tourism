from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url="/account/login/")
def index(request):
    return render(request, 'tour_guide/index.html')


@login_required(login_url="/account/login/")
def add_language(request):
    return render(request, 'tour_guide/add_lanugage.html')


@login_required(login_url="/account/login/")
def update_language(request):
    return render(request, 'tour_guide/update_lanugage.html')


@login_required(login_url="/account/login/")
def delete_language(request):
    return render(request, 'tour_guide/delete_language.html')


@login_required(login_url="/account/login/")
def tour_guide_profile_info(request):
    return render(request, 'tour_guide/tour_guide_profile_info.html')
