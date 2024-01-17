from rest_framework import serializers

from .models import UserTime, UserGivenScore


class UserTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTime
        fields = "__all__"


class UserGivenScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGivenScore
        fields = "__all__"
