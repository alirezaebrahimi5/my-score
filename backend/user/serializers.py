from rest_framework import serializers

from .models import Profile, User 


class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields =['identificationCode', 'mobile', 'phone', 'password', 'first_name', 'last_name',
                 'address', 'role']
        labels = {
            'password': 'گذر واژه',
        }
    
    def create(self, **validated_data):
        return super().create(validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'phone', 'first_name', 'last_name', 'role']
