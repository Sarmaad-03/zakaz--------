# Generated by Django 5.0.1 on 2024-03-06 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parfume', '0011_alter_parfume_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parfume',
            name='category',
            field=models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский'), ('Унисекс', 'Унисекс')], default=0, max_length=250),
            preserve_default=False,
        ),
    ]
