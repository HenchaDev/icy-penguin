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
        fields = ['age', 'sex', 'height', 'weight', 'bmi', 'vaccination_history', 'previous_medications', 'procedures', 'hospitalizations', 'current_symptoms']
        