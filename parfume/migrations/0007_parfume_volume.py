# Generated by Django 5.0.1 on 2024-02-21 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parfume', '0006_alter_parfume_options_alter_parfume_toilet_water'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parfume_volume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volum_ml', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('parfum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volumes', to='parfume.parfume')),
            ],
        ),
    ]
