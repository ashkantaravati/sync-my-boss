from django.contrib import admin
from django.urls import path, include
from employee_activity import views
from employee_activity.apis import (
    LogList,
    SubmitAvailabilityStatus,
    GetEmployeeInfo,
    GetWorkplaces,
    SetAttendance,
    WorkUpdateTypes,
    GetActivities,
    SubmitWorkUpdate,
    AvailabilityStatusTypes,
    PresentEmployees,
    AuthenticatedEmployee
    
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.dashboard),
    path("dashboard", views.dashboard),
    path("api/logs", LogList.as_view()),
    path("api/availability-statuses/create", SubmitAvailabilityStatus.as_view()),
    path("api/employee/<int:id>", GetEmployeeInfo.as_view()),
    path("api/employee/active", PresentEmployees.as_view()),
    path("api/employee/me", AuthenticatedEmployee.as_view()),
    path("api/workplace/all", GetWorkplaces.as_view()),
    path("api/attendance/set", SetAttendance.as_view()),
    path("api/types/workupdate", WorkUpdateTypes.as_view()),
    path("api/types/availability-status", AvailabilityStatusTypes.as_view()),
    path("api/activity/all-active", GetActivities.as_view()),
    path("api/workupdate", SubmitWorkUpdate.as_view()),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='employee_activity/login.html')),
    path("accounts/", include("django.contrib.auth.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# TODO user router