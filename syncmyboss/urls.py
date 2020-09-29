from django.contrib import admin
from django.urls import path
from employee_activity import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path("admin/", admin.site.urls), path("", views.dashboard)] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
