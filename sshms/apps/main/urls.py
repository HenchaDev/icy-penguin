from django.urls import path
from .views import home
from apps.users.views import user_login

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login/', user_login, name='login'),
]