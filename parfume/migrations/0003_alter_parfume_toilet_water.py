# Generated by Django 5.0.1 on 2024-02-07 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parfume', '0002_alter_parfume_toilet_water'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parfume',
            name='toilet_water',
            field=models.CharField(blank=True, choices=[('Есть', 'Есть'), ('Нету', 'Нету')], max_length=20, null=True),
        ),
    ]