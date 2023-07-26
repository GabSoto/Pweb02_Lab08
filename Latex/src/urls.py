from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.showForm, name="showForm"),
    path("register/", views.showRegister, name="showRegister"),
    path("home/", views.showHome, name="showHome")
]
