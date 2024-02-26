from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import SignUpForm, UserLoginForm, ProfileForm
from .models import UserProfile

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('complete_profile')
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
            return redirect('profile')
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
def edit_user_info(request):
    return render(request, 'users/edit_user_info_form.html')

@login_required
def save_user_info(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        # Get the current user
        user = request.user
        
        # Update the user's username and email
        user.username = username
        user.email = email
        user.save()
       
        messages.success(request, 'User info updated successfully.')
        return redirect('profile')
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)

@login_required
def edit_med_info(request):
    profile = request.user.userprofile
    return render(request, 'users/edit_med_info_form.html', {'profile': profile})

@login_required
def save_med_info(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        bmi = request.POST.get('bmi')
        
        profile = request.user.userprofile
        
        profile.age = age
        profile.sex = sex
        profile.height = height
        profile.weight = weight
        profile.bmi = bmi
        profile.save()
        
        messages.success(request, 'Medical info updated successfully.')
        return redirect('profile')
    else:
        return JsonResponse({'error': 'Method not allowed'})