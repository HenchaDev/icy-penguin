from django.urls import path
from .views import sign_up, user_login, complete_profile, view_profile, logout
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('signup/', sign_up, name='sign_up'),
    path('login/', user_login, name='login'),
    path('complete-profile/', complete_profile, name='complete_profile'),
    path('profile/', login_required(view_profile, login_url='/users/login/'), name='profile'),
    path('logout/', logout, name='logout'),
]