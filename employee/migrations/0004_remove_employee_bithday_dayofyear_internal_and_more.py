# Generated by Django 5.0.1 on 2024-03-13 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_is_emp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='bithday_dayofyear_internal',
        ),
        migrations.AlterField(
            model_name='employee',
            name='bithday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
