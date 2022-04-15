from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from tour_guide.models import Language, TourGuideProfile
from .forms import LanguageFrom, TourGuideProfileFrom


@login_required(login_url="/account/login/")
def index(request):
    languages = Language.objects.filter(user=request.user)
    return render(request, 'tour_guide/index.html', {'languages': languages})


@login_required(login_url="/account/login/")
def add_language(request):
    if request.method == "POST":
        form = LanguageFrom(request.POST, request.FILES)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            return redirect('tour_guide_home')
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:
        form = LanguageFrom()
    return render(request, 'tour_guide/add_language.html', {'form': form})


@login_required(login_url="/account/login/")
def update_language(request, id):
    language = Language.objects.get(id=id)
    if request.method == "POST":
        form = LanguageFrom(request.POST, request.FILES, instance=language)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            return redirect('tour_guide_home')
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:
        form = LanguageFrom(instance=language)
    return render(request, 'tour_guide/update_lanugage.html', {'form': form})


@login_required(login_url="/account/login/")
def delete_language(request, id):
    language = Language.objects.get(id=id)
    return render(request, 'tour_guide/delete_language.html', {'language': language})


@login_required(login_url="/account/login/")
def delete_language_check(request, id, check):
    language = Language.objects.get(id=id)
    if check:
        language.delete()
        return redirect('tour_guide_home')
    return render(request, 'tour_guide/delete_language.html',{'language':language})


@login_required(login_url="/account/login/")
def tour_guide_profile_info(request):
    try:
        profile = TourGuideProfile.objects.get(user=request.user)
    except TourGuideProfile.DoesNotExist:
        profile = None
    if request.method == "POST":
        form = TourGuideProfileFrom(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            shared_data = form.save(commit=False)
            shared_data.user = request.user
            shared_data.save()
            return redirect('tour_guide_home')
        else:
            print(form.errors)
            msg = 'Form is not valid'
    else:

        form = TourGuideProfileFrom(instance=profile)
    return render(request, 'tour_guide/tour_guide_profile_info.html',{'form':form})
