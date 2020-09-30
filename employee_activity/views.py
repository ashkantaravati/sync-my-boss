from django.shortcuts import render
from .serializers import LogSerializer
from .models import Log
from rest_framework import generics

def dashboard(request):
    if request.method == "GET":
        logs = Log.objects.all().order_by("-datetime_occured")
        username = "پریسا قمی"
        active_coworkers = 21
        latest_update = "شروع کار - پروژه‌ی آذرگستر - تغییر سایز هدر"
        status = "ترک میز برای ناهار"

        return render(
            request,
            "employee_activity/dashboard.html",
            {
                "logs": logs,
                "username": username,
                "status": status,
                "latest_update": latest_update,
                "active_coworkers": active_coworkers,
            },
        )

class LogList(generics.ListAPIView):
    queryset = Log.objects.all().order_by("-datetime_occured")
    serializer_class = LogSerializer