from rest_framework import serializers
from .models import Log, Employee, AvailabilityStatus, Workplace


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["first_name", "last_name", "job_title", "user", "full_name"]


class LogSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = Log
        fields = [
            "id",
            "datetime_occured_formatted",
            "employee",
            "event_message",
            "event_type",
        ]


class AvailabilityStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailabilityStatus
        fields = "__all__"


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = ["id", "name"]