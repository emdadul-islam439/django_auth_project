from django.contrib import admin
from django.urls import path
from basic_auth_app import views

urlpatterns = [
    path("", views.index, name = "home"),
]