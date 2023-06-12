from apps.authentication_app import views
from django.urls import path

urlpatterns = [
    path("register/", views.Register.as_view(), name="Register"),
    path("login/", views.Login.as_view(), name="Login"),
]
