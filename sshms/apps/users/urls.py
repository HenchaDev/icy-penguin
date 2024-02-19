from django.urls import path
from .views import sign_up, user_login, complete_profile, view_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', sign_up, name='sign_up'),
    path('login/', user_login, name='login'),
    path('complete-profile/', complete_profile, name='complete_profile'),
    path('profile/', view_profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]