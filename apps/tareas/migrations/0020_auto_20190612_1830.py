# Generated by Django 2.0.2 on 2019-06-13 00:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0019_auto_20190605_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotacionestarea',
            name='fecha_hora_anotacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 12, 18, 30, 8, 663208), null=True),
        ),
    ]
