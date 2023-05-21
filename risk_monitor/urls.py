from django.urls import path
from risk_monitor import views

urlpatterns = [
    path('', views.home, name='home'),
    path('settings/', views.settings, name='settings'),
    path('risk/<risk_id>', views.risk, name='risk'),
    path('get-risk-data/<risk_id>', views.get_risk_data),
    path('subscribe/<risk_id>', views.subscribe, name='subscribe'),
]