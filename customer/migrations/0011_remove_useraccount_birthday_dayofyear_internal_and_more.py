# Generated by Django 5.0.1 on 2024-03-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_purchase_parfume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='birthday_dayofyear_internal',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
