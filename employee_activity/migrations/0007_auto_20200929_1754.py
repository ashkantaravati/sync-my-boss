# Generated by Django 3.1.1 on 2020-09-29 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee_activity', '0006_auto_20200928_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.CharField(choices=[('Enter', 'ورود'), ('Exit', 'خروج')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AvailabilityStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(choices=[('Available', 'در دسترس'), ('In a Meeting', 'در جلسه'), ('Focusing', 'در حال تمرکز'), ('Busy', 'مشغول'), ('On Hourly Leave', 'در مرخصی ساعتی'), ('On Daily Leave', 'در مرخصی روزانه'), ('Left Work', 'سازمان را ترک کرده'), ('Away', 'ترک میز'), ('Away for a meal', 'ترک میز برای صرف وعده\u200cی غذایی')], max_length=20)),
                ('until', django_jalali.db.models.jDateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_occured', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('event_message', models.TextField()),
                ('event_type', models.CharField(max_length=40)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee_activity.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='EventLog',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='is_project',
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(choices=[('Sales', 'فروش'), ('Marketing', 'بازاریابی'), ('Project Management', 'مدیریت پروژه'), ('Operations', 'عملیا'), ('Human Resources', 'امور منابع انسانی'), ('Support', 'پشتیبانی'), ('Research and Development', 'تحقیق و توسعه'), ('Learning and Development', 'آموزش و توسعه'), ('Product Management', 'مدیریت محصول'), ('Finance', 'امور مالی'), ('Software Development', 'توسعه\u200cی نرم\u200cافزار'), ('Design', 'طراحی'), ('Search Engine Optimization', 'بهینه\u200cسازی موتور جستجو'), ('Contracts', 'امور قراردادها'), ('General', 'عمومی')], default='Standard', max_length=50),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='availabilitystatus',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee_activity.employee'),
        ),
        migrations.AddField(
            model_name='availabilitystatus',
            name='log',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee_activity.log'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee_activity.employee'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='log',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee_activity.log'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='workplace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee_activity.workplace'),
        ),
        migrations.AddField(
            model_name='workupdate',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee_activity.employee'),
        ),
        migrations.AddField(
            model_name='workupdate',
            name='log',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee_activity.log'),
        ),
    ]
