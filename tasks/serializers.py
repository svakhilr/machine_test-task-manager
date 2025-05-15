from rest_framework import serializers
from .models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class TaskUpdateSerializer(serializers.Serializer):
    completion_report = serializers.CharField()
    worked_hours = serializers.DecimalField(max_digits=10, decimal_places=2)
