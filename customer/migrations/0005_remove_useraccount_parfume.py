# Generated by Django 5.0.1 on 2024-02-11 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_useraccount_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='parfume',
        ),
    ]
