from django.contrib import admin
from django.urls import path
from employee_activity import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.dashboard),
    path("api/logs",views.LogList.as_view()),
    path("api/availability-statuses/create",views.SubmitAvailabilityStatus.as_view()),
    path("api/employee/<int:id>",views.GetEmployeeInfo.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
