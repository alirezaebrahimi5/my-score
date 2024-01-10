from rest_framework import serializers

<<<<<<< HEAD
from .models import UserLocation, NewLocation
=======
from .models import UserLocation
>>>>>>> f64a207 (adding some of location functionality)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = '__all__'
        exclude = ('created_at',)
        
        def create(self, validated_data):
            return UserLocation.objects.using("locations").create(**validated_data)
<<<<<<< HEAD


class NewLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewLocation
        fields = "__all__"
        exclude = ()
        
        def create(self, validated_data):
            return NewLocation.objects.create(**validated_data)
=======
>>>>>>> f64a207 (adding some of location functionality)
