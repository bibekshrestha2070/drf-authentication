from apps.authentication_app import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("register/", views.Register.as_view(), name="Register"),
    path("login/", views.Login.as_view(), name="Login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("profile/", views.UserAPIView.as_view(), name="user-info"),
    path("logout/", views.UserLogoutAPIView.as_view(), name="logout-user"),
]
