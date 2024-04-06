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
    path('logout/', views.logout_user, name='logout_user'),
    path('edit_demographic_info_form/', views.edit_demographic_info_form, name='edit_demographic_info_form'),
    path('edit_demographic_info/', views.edit_demographic_info, name='edit_demographic_info'),
    path('edit_medical_hist_form/', views.edit_medical_hist_form, name='edit_medical_hist_form'),
    path('edit_med_hist/', views.edit_med_hist, name='edit_med_hist'),
    path('edit_lifestyle_info_form/', views.edit_lifestyle_info_form, name='edit_lifestyle_info_form'),
    path('edit_lifestyle_info/', views.edit_lifestyle_info, name='edit_lifestyle_info'),
    path('edit_biometric_data/', views.edit_biometric_data, name='edit_biometric_data'),
    path('edit_biometric_data_form/', views.edit_biometric_data_form, name='edit_biometric_data_form'),
    path('edit_env_factors/', views.edit_env_factors, name='edit_env_factors'),
    path('edit_env_factors_form/', views.edit_env_factors_form, name='edit_env_factors_form'),    
]