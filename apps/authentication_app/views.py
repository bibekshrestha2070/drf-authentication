from apps.authentication_app import utils, serializers
from rest_framework.response import Response
import random
import string
from rest_framework import status
from apps.authentication_app.models import User
from django.db.models import Q

# Create your views here.


class Register(utils.BaseAPIView):

    """
    Signup user
    """

    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        request.data._mutable = True
        password = request.data.get("password")
        if not utils.password_check(password):
            return Response(
                {
                    "message": "Password should contain least 8 letter with least one lower or uppercase and should have at least one numeral and special characters"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        username = request.data.get("username")
        email = request.data.get("email")
        if not username:
            username = request.data.get("first_name", "") + "".join(
                random.choices(string.ascii_uppercase + string.digits, k=5)
            )
        request.data["username"] = username

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        db_user = User.objects.filter(Q(email=email) | Q(username=username)).first()
        if db_user:
            return Response({"message": "Duplicate email or username"}, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        return Response(
            {
                "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
            }
        )


class Login(utils.BaseAPIView):

    """
    Signin user
    """

    serializer_class = serializers.UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = serializers.CustomUserSerializer(user)

        token = utils.get_tokens_for_user(user=user)
        data = serializer.data
        data["tokens"] = token
        return Response(data, status=status.HTTP_201_CREATED)
