# Generated by Django 2.0.2 on 2019-06-24 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0023_auto_20190624_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotacionestarea',
            name='fecha_hora_anotacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 24, 14, 50, 36, 538666), null=True),
        ),
    ]