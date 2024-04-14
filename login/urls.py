from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.loginfunc, name='login'),
    path('register', views.register, name="register"),
    path('logout/', views.user_logout, name='logout'),

    # password reset urls
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='reset_pwd/pwd_reset_form.html'), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='reset_pwd/pwd_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_pwd/pwd_reset_confirm.html'), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_pwd/pwd_reset_complete.html'), name="password_reset_complete"),
    
]