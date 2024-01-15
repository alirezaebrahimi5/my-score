from rest_framework import serializers

from .models import VisitorTask, TaskDone


class DefineTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorTask
        fields = "__all__"
