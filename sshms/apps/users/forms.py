from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")
    


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'sex', 'ethnicity_race', 'socioeconomic_status', 'family_history_chronic_diseases', 'diagnosed_chronic_conditions', 'medications', 'surgeries', 'typical_daily_diet', 'physical_activity_frequency', 'smoking_habits', 'alcohol_consumption', 'recreational_drug_use', 'stress_management_methods', 'height', 'weight', 'blood_pressure', 'cholesterol_levels', 'blood_glucose_levels', 'air_pollution_exposure', 'occupational_hazards', 'clean_drinking_water_access', 'genetic_conditions', 'genetic_testing_results', 'medical_compliance', 'health_literacy', 'mental_health_diagnosis', 'social_support_network', 'occupation', 'work_stress', 'last_checkup', 'cancer_screening', 'residential_area', 'access_to_healthcare', 'additional_comments']


class DemographicInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'sex', 'ethnicity_race', 'socioeconomic_status']   
        
class MedicalHistForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['family_history_chronic_diseases', 'diagnosed_chronic_conditions', 'medications', 'surgeries']
        
class LifestyleInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['typical_daily_diet', 'physical_activity_frequency', 'smoking_habits', 'alcohol_consumption', 'recreational_drug_use', 'stress_management_methods']
        
class BiometricDataForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['height', 'weight', 'blood_pressure', 'cholesterol_levels', 'blood_glucose_levels']
        
class EnvironmentalFactorsForm(forms.Form):
    air_pollution_exposure = forms.BooleanField(required=False)
    occupational_hazards = forms.BooleanField(required=False)
    clean_drinking_water_access = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['air_pollution_exposure'].widget = forms.Select(choices=[(True, 'Yes'), (False, 'No')])
        self.fields['occupational_hazards'].widget = forms.Select(choices=[(True, 'Yes'), (False, 'No')])
        self.fields['clean_drinking_water_access'].widget = forms.Select(choices=[(True, 'Yes'), (False, 'No')])