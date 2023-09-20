# In your app's serializers.py
from rest_framework import serializers
from .models import UserProfile

class UserProfileRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user_id', 'first_name', 'last_name', 'phone', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user_profile = UserProfile.objects.create(**validated_data)
        return user_profile



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

