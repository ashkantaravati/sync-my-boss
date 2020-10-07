from .serializers import LogSerializer, AvailabilityStatusSerializer, EmployeeSerializer
from .models import Log, AvailabilityStatus, Employee
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
