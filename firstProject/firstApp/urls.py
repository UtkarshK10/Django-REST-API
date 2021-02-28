# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path,include
from firstApp import views

urlpatterns = [
    path('emps/',views.employeeView),
]