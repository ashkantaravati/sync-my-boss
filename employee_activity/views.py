from django.shortcuts import render
from .serializers import LogSerializer, AvailabilityStatusSerializer
from .models import Log, AvailabilityStatus
from rest_framework import generics
from jdatetime import datetime

def dashboard(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            # Do something for authenticated users.
            current_user = request.user
            current_employee = current_user.employee 
            today = datetime.now().strftime("%a, %d %b %Y")
            logs = Log.objects.all().order_by("-datetime_occured")
            active_coworkers = 21
            latest_update = "شروع کار - پروژه‌ی آذرگستر - تغییر سایز هدر"
            status = "ترک میز برای ناهار"

            return render(
                request,
                "employee_activity/dashboard.html",
                {
                    "logs": logs,
                    "username": current_employee,
                    "status": status,
                    "latest_update": latest_update,
                    "active_coworkers": active_coworkers,
                    "today":today
                },
            )
        else:
            pass

class LogList(generics.ListAPIView):
    queryset = Log.objects.all().order_by("-datetime_occured")
    serializer_class = LogSerializer


class SubmitAvailabilityStatus(generics.CreateAPIView):
    queryset = AvailabilityStatus.objects.all()
    serializer_class = AvailabilityStatusSerializer