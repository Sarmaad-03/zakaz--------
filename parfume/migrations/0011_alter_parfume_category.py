# Generated by Django 5.0.1 on 2024-02-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parfume', '0010_remove_parfume_price_remove_parfume_volum_ml_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parfume',
            name='category',
            field=models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский'), ('Унисекс', 'Унисекс')], default=None, max_length=250, null=True, blank = True),
        ),
    ]
