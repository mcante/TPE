# Generated by Django 2.0.2 on 2019-06-05 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0017_auto_20190531_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotacionestarea',
            name='fecha_hora_anotacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 5, 13, 7, 13, 252365), null=True),
        ),
    ]
