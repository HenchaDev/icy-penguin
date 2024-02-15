from django.urls import path
from .views import sign_up, user_login

urlpatterns = [
    path('signup/', sign_up, name='sign_up'),
    path('', user_login, name='login')
]