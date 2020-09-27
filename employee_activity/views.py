from django.shortcuts import render
from .models import EventLog


def all_activities(request):
    if request.method == "GET":
        logs = EventLog.objects.all() #.order_by("-datetime_submitted")
        return render(
            request,
            "employee_activity/all-activities.html",
            {"activities": logs},
        )
