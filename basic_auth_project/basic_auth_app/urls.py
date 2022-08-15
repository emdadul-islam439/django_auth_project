from django.contrib import admin
from django.urls import path
from basic_auth_app import views

urlpatterns = [
    path("", views.index, name = "home"),
    path("login", views.loginUser, name = "loginUser"),
    path("logout", views.logoutUser, name = "logoutUser")
]