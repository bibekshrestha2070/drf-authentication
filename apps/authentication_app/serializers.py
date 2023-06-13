from rest_framework import serializers
from apps.authentication_app.models import User
from django.contrib.auth import authenticate

# Register serializer


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "first_name", "last_name", "email")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
        )
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class to authenticate users with email and password.
    """

    username = serializers.CharField(label="Username", write_only=True)
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(request=self.context.get("request"), username=username, password=password)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize CustomUser model.
    """

    class Meta:
        model = User
        fields = ("id", "username", "email")


class UserLogoutSerializer(serializers.Serializer):

    refresh = serializers.CharField(required=True)
    print("a")

    def validate(self, data):
        error = dict()

        if "refresh" not in data:
            error["refresh"] = "This field is required"
        if not len(error) == 0:
            raise serializers.ValidationError(error)
        return data
