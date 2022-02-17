from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password

class RegisterUserSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    def validate(self, value):
        if value['password'] != value['password_2']:
            raise serializers.ValidationError("password and confirm password must match!")
        return value
    
    def create(self, validated_data):
        validated_data.pop("password_2")
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def get_token(self, user):
        token = RefreshToken.for_user(user)
        refresh = str(token)
        access = str(token.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data

    class Meta: 
        model = User
        fields = ('id', 'email', 'name', 'password', 'password_2', 'created', 'modified', 'token')
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'name'
        ]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'name': self.user.name})
        data.update({'id': self.user.id})
        data.update({'email' : self.user.email})
        return data