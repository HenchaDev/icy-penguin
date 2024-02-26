from django.urls import path
# from .views import sign_up, user_login, complete_profile, view_profile, logout, edit_user_info, save_user_info,
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.user_login, name='login'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
    path('profile/', login_required(views.view_profile, login_url='/users/login/'), name='profile'),
    path('logout/', views.logout, name='logout'),
    path('edit_user_info/', views.edit_user_info, name='edit_user_info'),
    path('save_user_info/', views.save_user_info, name='save_user_info'),
    path('edit_med_info/', views.edit_med_info, name='edit_med_info'),
    path('save_med_info/', views.save_med_info, name='save_med_info'),
]