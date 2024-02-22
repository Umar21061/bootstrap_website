# practice/urls.py
from django.contrib import admin
from django.urls import path, include   # Import include
from user import views                  # Import views from the user app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Set the default URL to the home page
    path('', include('user.urls')),     # Include URLs from the user app
]
