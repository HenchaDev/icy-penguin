from django.shortcuts import render
from apps.prediction.models import Prediction

# Create your views here.
def home(request):
    user_predictions = request.user.predictions.all()
    context = {
        'predictions': user_predictions,
    }
    return render(request, 'main/home.html', context)