from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from apps.prediction.models import Prediction


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        user_predictions = request.user.predictions.all()
    else:
        user_predictions = None
    
    context = {
        'predictions': user_predictions
    }
    
    return render(request, 'main/home.html', context)

def homely(request):
    return render(request, 'main/homely.html')

class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.session.session_key is None:
            return redirect('users:login')
        
        if request.session.get_expire_at_browser_close():
            messages.error(request, 'Your sessin has expired. Please login again.')
            request.session.flush()
            show_login_popup = True
        else:
            show_login_popup = False
        
        context = {'show_login_popup': show_login_popup}    
        return super().dispatch(request, *args, **kwargs, context=context)