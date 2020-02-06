from django.shortcuts import render,redirect


from rest_framework import viewsets

from webapp.models import User
from webapp.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

