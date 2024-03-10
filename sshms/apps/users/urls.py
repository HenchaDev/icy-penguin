from django.urls import path
# from .views import sign_up, user_login, complete_profile, view_profile, logout, edit_user_info, save_user_info,
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.user_login, name='login'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
    path('profile/', login_required(views.view_profile, login_url='/users/login/'), name='profile'),
    path('logout/', views.logout, name='logout'),
    path('edit_demographic_info_form/', views.edit_demographic_info_form, name='edit_demographic_info_form'),
    path('edit_demographic_info/', views.edit_demographic_info, name='edit_demographic_info'),
]