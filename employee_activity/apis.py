from .serializers import (
    LogSerializer,
    AvailabilityStatusSerializer,
    EmployeeSerializer,
    WorkplaceSerializer,
    AttendanceSerializer,
)
from .models import Log, AvailabilityStatus, Employee, Workplace, Attendance
from rest_framework import generics


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
