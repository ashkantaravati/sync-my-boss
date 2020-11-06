from rest_framework import serializers
from .models import Log, Employee, AvailabilityStatus, Workplace, Attendance, Activity, WorkUpdate


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "first_name",
            "last_name",
            "job_title",
            "user",
            "full_name",
            "current_availability_status",
            "current_availability_status_text",
            "current_availability_status_class",
            "current_work_update",
            "is_present_now"
        ]


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


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ["employee", "action_type", "workplace"]


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"

        
class WorkUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkUpdate
        fields = "__all__"