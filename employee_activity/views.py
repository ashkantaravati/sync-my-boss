from django.shortcuts import render
from .utils import get_today_formatted_jdatetime
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    if request.method == "GET":
        current_user = request.user
        current_employee = current_user.employee
        current_employee_id = current_employee.pk
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