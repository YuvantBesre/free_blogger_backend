from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import RegisterUserSerializer, CustomTokenObtainPairSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterUser(CreateAPIView):
    def create(self, request):
        serialized_data = RegisterUserSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            self.perform_create(serialized_data)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

class ValidateUser(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer