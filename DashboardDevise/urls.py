from django.contrib import admin
from django.urls import path

from devise.views import dashboard, redirect_index

urlpatterns = [
    path('', redirect_index, name='index'),
    path('home/', dashboard, name='home'),
    path('home/<int:days_range>/<str:currencies>/', dashboard, name='home_with_params'),
    path('admin/', admin.site.urls),
]