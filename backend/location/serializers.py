from rest_framework import serializers

from .models import UserLocation, NewLocation


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = '__all__'
        exclude = ('created_at',)
        
        def create(self, validated_data):
            return UserLocation.objects.using("locations").create(**validated_data)


class NewLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewLocation
        fields = "__all__"
        exclude = ()
        
        def create(self, validated_data):
            return NewLocation.objects.create(**validated_data)
