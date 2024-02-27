from django.urls import path
from . import views

app_name = 'prediction'

urlpatterns = [
    path('', views.generate_text, name='generate_texts'),
]