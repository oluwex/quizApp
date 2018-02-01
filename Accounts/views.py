#from django.shortcuts import render

# Create your views here.

from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer

User = get_user_model()

class UserRegisterView(CreateAPIView):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        
        return Response(user,
                        status=status.HTTP_201_CREATED,
                        headers=headers)
    