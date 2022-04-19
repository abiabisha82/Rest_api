from django.shortcuts import render
from profiles_api import models
from profiles_api import permissions
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import Token 
from profiles_user import serializers
from rest_framework import viewsets
# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
