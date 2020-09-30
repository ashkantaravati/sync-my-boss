from rest_framework import serializers
from .models import Log, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    
    class Meta:
        model = Log
        fields = ["id", "datetime_occured", "employee", "event_message", "event_type"]
