from django.shortcuts import render
from .serializers import LogSerializer, AvailabilityStatusSerializer, EmployeeSerializer
from .models import Log, AvailabilityStatus, Employee
from rest_framework import generics
from .utils import get_today_formatted_jdatetime


def dashboard(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            # Do something for authenticated users.
            current_user = request.user
            current_employee = current_user.employee
            current_employee_id = current_employee.pk
            today = datetime.now().strftime("%a, %d %b %Y")
            active_coworkers = 21

            return render(
                request,
                "employee_activity/dashboard.html",
                {
                    "current_employee_id": current_employee_id,
                    "active_coworkers": active_coworkers,
                    "today": get_today_formatted_jdatetime(),
                },
            )
        else:
            pass
