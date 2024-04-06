from django.urls import path
from . import views
# from apps.users.views import user_login

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    # path('accounts/login/', user_login, name='login'),
]