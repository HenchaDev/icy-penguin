from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import EnvironmentalFactorsForm, BiometricDataForm, LifestyleInfoForm, SignUpForm, UserLoginForm, ProfileForm, DemographicInfoForm, MedicalHistForm
from .models import UserProfile
from apps.prediction.models import Prediction

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
                
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('main:home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = UserLoginForm()
        
    context = {
        'form': form,
        'next': request.GET.get('next', '')
    }
    
    return render(request, 'users/login.html', context)

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
        
    user_predictions = request.user.predictions.all()
    context = {
        'profile': profile,
        'predictions': user_predictions,
    }
    return render(request, 'users/profile.html', context)

def logout_user(request):
    logout(request)
    request.session.flush()
    # return redirect('users:login')
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

@login_required
def edit_medical_hist_form(request):
    profile = request.user.userprofile
    form = MedicalHistForm(instance=profile)
    return render(request, 'users/edit_med_hist_form.html', {'form': form})

@login_required
def edit_med_hist(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = MedicalHistForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return JsonResponse({
                'success': True,
                'family_history_chronic_diseases': profile.family_history_chronic_diseases,
                'diagnosed_chronic_conditions': profile.diagnosed_chronic_conditions,
                'medications': profile.medications,
                'surgeries': profile.surgeries
            })
        else:
            return JsonResponse({'success': False, 'message': 'Form is invalid'})
    else:
        form = MedicalHistForm(instance=profile)
        
    return render(request, 'users/edit_med_hist_form.html', {'form': form})


@login_required
def edit_lifestyle_info_form(request):
    profile = request.user.userprofile
    form = LifestyleInfoForm(instance=profile)
    return render(request, 'users/edit_lifestyle_info_form.html', {'form': form})

@login_required
def edit_lifestyle_info(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = LifestyleInfoForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return JsonResponse({
                'success': True,
                'typical_dail_diet': profile.typical_daily_diet,
                'physical_activity_frequency': profile.physical_activity_frequency,
                'smoking_habits': profile.smoking_habits,
                'alcohol_consumption': profile.alcohol_consumption,
                'recreational_drug_use': profile.recreational_drug_use,
                'stress_management_methods': profile.stress_management_methods
            })
        else:
            return JsonResponse({'success': False, 'message': 'Form is invalid'})
    else:
        form = LifestyleInfoForm(instance=profile)
        
    return render(request, 'users/edit_lifestyle_info_form.html', {'form': form})

@login_required
def edit_biometric_data_form(request):
    profile = request.user.userprofile
    form = BiometricDataForm(instance=profile)
    return render(request, 'users/edit_biometric_data_form.html', {'form': form})

@login_required
def edit_biometric_data(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = BiometricDataForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return JsonResponse({
                'success': True,
                'height': profile.height,
                'weight': profile.weight,
                'blood_pressure': profile.blood_pressure,
                'cholesterol_levels': profile.cholesterol_levels,
                'blood_glucose_levels': profile.blood_glucose_levels
            })
        else:
            return JsonResponse({'success': False, 'message': 'Form is invalid'})
    else:
        form = BiometricDataForm(instance=profile)
    
    return render(request, 'users/edit_biometric_data_form.html', {'form': form})\
 
@login_required
def edit_env_factors_form(request):
    return render(request, 'users/edit_env_factors_form.html', {'form': EnvironmentalFactorsForm()})

@login_required
def edit_env_factors(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = EnvironmentalFactorsForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return JsonResponse({
                'success': True,
                'air_pollution_exposure': profile.air_pollution_exposure,
                'occupational_hazards': profile.occupational_hazards,
                'clean_drinking_water_access': profile.clean_drinking_water_access
            })
        else:
            return JsonResponse({'success': False, 'message': 'Form is invalid!'})
    else:
        form = EnvironmentalFactorsForm(instance=profile)
        return render(request, 'users/edit_env_factors_form.html', {'form': form})
