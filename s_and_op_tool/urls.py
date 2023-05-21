from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('monitor/', include('risk_monitor.urls')),
    path('user/', include('users_app.urls')),
]
