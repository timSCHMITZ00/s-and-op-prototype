from django.urls import path
from users_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('log-in/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('log-out/', auth_views.LogoutView.as_view(), name='logout'),
]