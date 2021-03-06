from django.contrib import admin
from django.urls import path,include
from employee_activity import views
from employee_activity.apis import (
    LogList,
    SubmitAvailabilityStatus,
    GetEmployeeInfo,
    GetWorkplaces,
    SetAttendance,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.dashboard),
    path("api/logs", LogList.as_view()),
    path("api/availability-statuses/create", SubmitAvailabilityStatus.as_view()),
    path("api/employee/<int:id>", GetEmployeeInfo.as_view()),
    path("api/workplace/all", GetWorkplaces.as_view()),
    path("api/attendance/set", SetAttendance.as_view()),
    path("accounts/", include("django.contrib.auth.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# TODO user router