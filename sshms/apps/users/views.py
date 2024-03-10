from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import SignUpForm, UserLoginForm, ProfileForm, DemographicInfoForm
from .models import UserProfile

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:complete_profile')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:home')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form':form})

@login_required
def complete_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('users:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/complete_profile.html', {'form': form})

@login_required
def view_profile(request):
    try:
        # profile = UserProfile(user=request.user)
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = None
    return render(request, 'users/profile.html', {'profile': profile})

def logout(request):
    return render(request, 'users/logout.html')


@login_required
def edit_demographic_info_form(request):
    profile = request.user.userprofile
    form = DemographicInfoForm(instance=profile)
    return render(request, 'users/demographic_info_form.html', {'form': form})

@login_required
def edit_demographic_info(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = DemographicInfoForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return JsonResponse({
                'success': True,
                'age': profile.age,
                'sex': profile.sex,
                'ethnicity_race': profile.ethnicity_race,
                'socioeconomic_status': profile.socioeconomic_status
            })
        else:
            return JsonResponse({'success': False, 'message': 'Form is invalid'})
    else:
        form = DemographicInfoForm(instance=profile)

    return render(request, 'users/demographic_info_form.html', {'form': form})