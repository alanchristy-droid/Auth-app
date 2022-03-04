from django import views
from django.contrib import admin
from django.urls import path
from .views import RegisterAPI
from .views import LoginAPI
from knox import views as knox_views

urlpatterns = [
    path('operation/register/', RegisterAPI.as_view(), name='register'),
    path('operation/login/', LoginAPI.as_view(), name='login'),
    path('operation/logout/', knox_views.LogoutView.as_view(), name='logout'),
]
