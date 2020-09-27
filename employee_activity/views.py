from django.shortcuts import render
from .models import EventLog


def dashboard(request):
    if request.method == "GET":
        logs = EventLog.objects.all().order_by("-datetime_submitted")
        return render(
            request,
            "employee_activity/dashboard.html",
            {"logs": logs},
        )
