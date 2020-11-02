from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from .utils import get_kebab_case, get_formatted_jdatetime

# from .model_mixins import LogMixin
from .value_choices import (
    WORK_UPDATE_TYPES,
    ATTENDANCE_ACTION_TYPES,
    AVAILABILITY_STATUS_REASON_TYPES,
    ACTIVITY_TYPES,
    DAYLONG_STATUS_TYPES,
    INDEFINITE_STATUS_TYPES,
)


class Employee(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    job_title = models.CharField(max_length=100, verbose_name="عنوان شغل")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر")

    class Meta:
        verbose_name = "کارمند"
        verbose_name_plural = "کارمندان"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_title}"

    @property
    def current_availability_status(self):
        return (
            AvailabilityStatus.objects.filter(employee=self)
            .order_by("-datetime_occured")
            .first()
            .reason
        )

    @property
    def current_availability_status_text(self):
        return (
            AvailabilityStatus.objects.filter(employee=self)
            .order_by("-datetime_occured")
            .first()
            .get_reason_display()
        )

    @property
    def current_work_update(self):
        return (
            WorkUpdate.objects.filter(employee=self)
            .order_by("-datetime_occured")
            .first()
            .__str__()
        )

    @property
    def current_availability_status_class(self):
        return get_kebab_case(self.current_availability_status)


class LogMixin(models.Model):
    log = models.OneToOneField("Log", on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE, default=1)
    datetime_occured = jmodels.jDateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def get_type_info(self):
        pass

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        _log = Log(
            employee=self.employee,
            event_message=str(self),
            event_type=self.get_type_info(),
        )
        _log.save()
        self.log = _log


class Log(models.Model):
    objects = jmodels.jManager()
    datetime_occured = jmodels.jDateTimeField(auto_now_add=True)
    employee = models.ForeignKey("Employee", on_delete=models.SET_NULL, null=True)
    event_message = models.TextField()
    event_type = models.CharField(max_length=40)

    class Meta:
        verbose_name = "لاگ"
        verbose_name_plural = "لاگ‌ها"

    @property
    def datetime_occured_formatted(self):
        return get_formatted_jdatetime(self.datetime_occured)

    def __str__(self):
        return f"{self.datetime_occured_formatted} - {self.event_message}"


class Activity(models.Model):
    name = models.CharField(max_length=50, verbose_name="موضوع فعالیت")
    activity_type = models.CharField(
        max_length=50, choices=ACTIVITY_TYPES, default="Standard", verbose_name="نوع فعالیت"
    )

    class Meta:
        verbose_name = "فعالیت"
        verbose_name_plural = "فعالیت‌ها"

    def __str__(self):
        return f"{self.get_activity_type_display()} - {self.name}"


class WorkUpdate(LogMixin):
    update_type = models.CharField(max_length=20, choices=WORK_UPDATE_TYPES)
    activity = models.ForeignKey("Activity", on_delete=models.SET_NULL, null=True)
    work_title = models.CharField(max_length=200)
    notes = models.TextField(null=True, blank=True)
    estimated_remaining_time = models.DurationField()

    class Meta:
        verbose_name = "اعلان کاری"
        verbose_name_plural = "اعلانات کاری"

    def get_type_info(self):
        return self.get_update_type_display()

    def __str__(self):
        return f"{self.get_type_info()}: {self.activity} - {self.work_title} "


class Workplace(models.Model):
    name = models.CharField(max_length=40, verbose_name="مکان")

    class Meta:
        verbose_name = "محل کار"
        verbose_name_plural = "محل‌های کار"

    def __str__(self):
        return self.name


class Attendance(LogMixin):
    workplace = models.ForeignKey("Workplace", on_delete=models.SET_NULL, null=True, verbose_name= "محل کار")
    action_type = models.CharField(max_length=10, choices=ATTENDANCE_ACTION_TYPES, verbose_name="نوع فعالیت")

    class Meta:
        verbose_name = "سابقه‌ی حضور و غیاب"
        verbose_name_plural = "سوابق حضور و غیاب"

    def get_type_info(self):
        return self.get_action_type_display()

    def __str__(self):
        return f"{self.get_type_info()}: {self.employee} - {self.workplace}"


class AvailabilityStatus(LogMixin):
    objects = jmodels.jManager()
    reason = models.CharField(max_length=20, choices=AVAILABILITY_STATUS_REASON_TYPES)
    until = jmodels.jDateTimeField()

    class Meta:
        verbose_name = "وضعیت کارمند"
        verbose_name_plural = "وضعیت‌های کارمند"

    def get_type_info(self):
        return self.get_reason_display()

    @property
    def until_formatted(self):
        object_type = "date" if self.reason in DAYLONG_STATUS_TYPES else "datetime"
        formatted_datetime = get_formatted_jdatetime(
            self.until, object_type=object_type, show_seconds=False
        )
        return formatted_datetime

    def __str__(self):
        until_details = (
            "" if self.reason in INDEFINITE_STATUS_TYPES else f" تا {self.until_formatted}"
        )
        return f"{self.employee} - {self.get_reason_display()} {until_details}"
