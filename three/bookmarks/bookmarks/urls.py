from django.contrib import admin
from django.urls import path, include
from account.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('account/', include('account.urls')),
]
