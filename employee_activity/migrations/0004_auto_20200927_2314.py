# Generated by Django 3.1.1 on 2020-09-27 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_activity', '0003_activitylog_datetime_submitted'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ActivityLog',
            new_name='EventLog',
        ),
    ]