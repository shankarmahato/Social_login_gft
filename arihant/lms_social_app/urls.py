from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('accounts/', include('allauth.urls')),
    path("", views.home, name="home"),
]