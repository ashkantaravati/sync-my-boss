# Generated by Django 3.1.1 on 2020-09-29 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_activity', '0007_auto_20200929_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='log',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_activity.log'),
        ),
        migrations.AlterField(
            model_name='availabilitystatus',
            name='log',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_activity.log'),
        ),
        migrations.AlterField(
            model_name='workupdate',
            name='log',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_activity.log'),
        ),
    ]