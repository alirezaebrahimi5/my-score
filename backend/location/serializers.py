from rest_framework import serializers

from .models import UserLocation


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = '__all__'
        exclude = ('created_at',)
        
        def create(self, validated_data):
            return UserLocation.objects.using("locations").create(**validated_data)
