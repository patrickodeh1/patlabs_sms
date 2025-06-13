from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
