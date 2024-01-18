from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import Profile, User 


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize CustomUser model.
    """

    class Meta:
        model = User
        fields = ("id", "phone", "identificationCode", "mobile", "first_name", "last_name", "address", "role")


class LoginUserSerializer(serializers.Serializer):
    mobile = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields =['identificationCode', 'mobile', 'phone', 'password', 'first_name', 'last_name',
                 'address', 'role']
        labels = {
            'password': 'گذر واژه',
        }
    
    def create(self, **validated_data):
        return User.objects.create_user(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'phone', 'first_name', 'last_name', 'role']
