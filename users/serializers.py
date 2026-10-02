from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import UserPreference

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)
  password2 = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'password', 'password2']

  def validate_data(self, attrs):
    if(attrs['password'] != attrs['passoword2']):
      raise serializers.ValidationError({
        'password': "passwords do not match"
      })

    validate_password(attrs['password'])

    return attrs

  def create(self, validated_data):
    validated_data.pop('password2')
    return User.objects.create_user(**validated_data)   

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'email']

class UserPreferenceSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserPreference
    fields = [
      "dietary_preference",
      "budget_min",
      "budget_max",
      "favourite_cuisines",
      "max_distance"
    ]
