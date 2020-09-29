from django.contrib import admin
from .models import (
    Log,
    Employee,
    Activity,
    WorkUpdate,
    Workplace,
    Attendance,
    AvailabilityStatus,
)

admin.site.register(Employee)
admin.site.register(Activity)
admin.site.register(Workplace)
admin.site.register(WorkUpdate)
admin.site.register(Attendance)
admin.site.register(AvailabilityStatus)

from django_jalali.admin.filters import JDateFieldListFilter

# you need import this for adding jalali calander widget
import django_jalali.admin as jadmin


class LogAdmin(admin.ModelAdmin):
    list_filter = (("datetime_occured", JDateFieldListFilter),)


admin.site.register(Log, LogAdmin)

admin.site.site_header = "پنل مدیریت سامانه گردش اطلاعات سازمانی"
