from django.urls import path
from .views import sign_up, user_login, complete_profile, view_profile, logout, edit_user_info, save_user_info
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('signup/', sign_up, name='sign_up'),
    path('login/', user_login, name='login'),
    path('complete-profile/', complete_profile, name='complete_profile'),
    path('profile/', login_required(view_profile, login_url='/users/login/'), name='profile'),
    path('logout/', logout, name='logout'),
    path('edit_user_info/', edit_user_info, name='edit_user_info'),
    path('save_user_info/', save_user_info, name='save_user_info'),
]