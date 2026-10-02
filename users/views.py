from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import RegisterSerializer, ProfileSerializer, UserPreferenceSerializer
from .models import UserPreference

class RegisterView(generics.CreateAPIView):
  serializer_class = RegisterSerializer
  permission_classes = [AllowAny]

class ProfileView(generics.RetrieveUpdateAPIView):
  serializer_class = ProfileSerializer
  permission_classes = [IsAuthenticated]

  def get_object(self):
    return self.request.user

class UserPreferenceView(generics.RetrieveUpdateAPIView):
  serializer_class = UserPreferenceSerializer
  permission_classes = [IsAuthenticated]

  def get_object(self):
    preference, created = UserPreference.objects.get_or_create(
      user = self.request.user
    )

    return preference
  