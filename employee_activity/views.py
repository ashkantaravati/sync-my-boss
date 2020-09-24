from django.shortcuts import render
from .models import ActivityLog


def all_activities(request):
    if request.method == "GET":
        activities = ActivityLog.objects.all() #.order_by("-datetime_submitted")
        return render(
            request,
            "employee_activity/all-activities.html",
            {"activities": activities},
        )
