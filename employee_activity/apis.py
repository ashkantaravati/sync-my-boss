from .serializers import (
    LogSerializer,
    AvailabilityStatusSerializer,
    EmployeeSerializer,
    WorkplaceSerializer,
    AttendanceSerializer,
    ActivitySerializer,
    WorkUpdateSerializer,
)
from .models import (
    Log,
    AvailabilityStatus,
    Employee,
    Workplace,
    Attendance,
    Activity,
    WorkUpdate,
)
from rest_framework import generics, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .value_choices import WORK_UPDATE_TYPES, AVAILABILITY_STATUS_REASON_TYPES
from .utils import get_choices_as_json_serializable


class LogList(generics.ListAPIView):
    queryset = Log.objects.all().order_by("-datetime_occured")
    serializer_class = LogSerializer


class SubmitAvailabilityStatus(generics.CreateAPIView):
    queryset = AvailabilityStatus.objects.all()
    serializer_class = AvailabilityStatusSerializer


class GetEmployeeInfo(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    lookup_field = "id"
    serializer_class = EmployeeSerializer


class GetWorkplaces(generics.ListAPIView):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer


class SetAttendance(generics.CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class WorkUpdateTypes(APIView):
    def get(self, request):
        update_types = get_choices_as_json_serializable(
            WORK_UPDATE_TYPES, "update_type", "update_type_display"
        )
        return Response(update_types)


class AvailabilityStatusTypes(APIView):
    def get(self, request):
        update_types = get_choices_as_json_serializable(
            AVAILABILITY_STATUS_REASON_TYPES, "reason", "reason_display"
        )
        return Response(update_types)


class GetActivities(generics.ListAPIView):
    queryset = Activity.objects.filter(is_archived=False)
    serializer_class = ActivitySerializer


class SubmitWorkUpdate(generics.CreateAPIView):
    queryset = WorkUpdate.objects.all()
    serializer_class = WorkUpdateSerializer


class PresentEmployees(APIView):
    def get(self, request):
        # TODO we should check which employee's requesting so we can exclude them from the report
        present_employees = Employee.objects.filter(is_present_now=True)
        present_employee_report = {
            "numberOfPresentEmployees": len(present_employees),
            "numberOfPresentCoworkers": len(present_employees) - 1,
            "presentEmployeesData": [
                employee.full_name for employee in present_employees
            ],
        }
        return Response(present_employee_report)