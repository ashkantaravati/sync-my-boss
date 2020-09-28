from django.db import models
from django_jalali.db import models as jmodels


class EventLog(models.Model):
    objects = jmodels.jManager()
    employee = models.CharField(max_length=200)
    datetime_occured = jmodels.jDateTimeField()


UPDATE_TYPE_CHOICES = (
    ("Work Started", "کار شروع شد"),
    ("Work Paused", "کار متوقف شد"),
    ("Work Stuck", "کار با مانع رو به رو شد"),
    ("Work Advanced", " کار در حال پیشروی است"),
    ("Work Succeeded", "کار با موفقیت پایان یافت"),
    ("Work Canceled", "کار لغو شد"),
    ("Work Failed", "کار با شکست مواجه شد"),
)


class WorkUpdate(models.Model):
    update_type = models.CharField(max_length=20, choices=UPDATE_TYPE_CHOICES)
    activity = models.ForeignKey("Activity", on_delete=models.SET_NULL, null=True)
    work_title = models.CharField(max_length=200)
    notes = models.TextField()
    estimated_remaining_time = models.DurationField()


class Activity(models.Model):
    name = models.CharField(max_length=100)
    is_project = models.BooleanField()