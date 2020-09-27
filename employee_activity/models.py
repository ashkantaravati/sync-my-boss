from django.db import models
from django_jalali.db import models as jmodels

class EventLog(models.Model):
    objects = jmodels.jManager()
    employee = models.CharField(max_length=200)
    previous_efforts = models.TextField()
    next_efforts = models.TextField()
    impediments = models.TextField()
    other_notable_feedback = models.TextField()
    datetime_submitted = jmodels.jDateTimeField()
    from_time = jmodels.jDateTimeField()
    to_time = jmodels.jDateTimeField()

