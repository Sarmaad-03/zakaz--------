# Generated by Django 5.0.1 on 2024-02-11 11:42

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_remove_useraccount_dob_useraccount_birthday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]