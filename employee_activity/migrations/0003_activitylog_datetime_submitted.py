# Generated by Django 3.1.1 on 2020-09-24 11:00

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_activity', '0002_auto_20200924_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitylog',
            name='datetime_submitted',
            field=django_jalali.db.models.jDateTimeField(default='1399-01-01'),
            preserve_default=False,
        ),
    ]
