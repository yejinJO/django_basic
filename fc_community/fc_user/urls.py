from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout)
]
