# Generated by Django 5.0.1 on 2024-03-15 12:04

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_remove_useraccount_birthday_dayofyear_internal_and_more'),
        ('parfume', '0013_alter_parfume_volume_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parfume', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gifts', to='parfume.parfume_volume')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gifts', to='customer.useraccount')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
