
from django.contrib import admin
from django.urls import path,include
from firstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstApp/',include('firstApp.urls')),
]
