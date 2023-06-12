import re
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken


class BaseAPIView(generics.GenericAPIView):
    pass


def password_check(passwd):
    # pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!]).*$"
    pattern = "^.*(?=.{8,}).*$"
    return re.findall(pattern, passwd)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
