# Generated by Django 2.0.2 on 2019-04-09 20:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0012_auto_20190409_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotacionestarea',
            name='fecha_hora_anotacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 9, 14, 56, 47, 744480), null=True),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='fecha_hora_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 9, 14, 56, 47, 743480), null=True),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='fecha_hora_planificada',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 9, 14, 56, 47, 743480), null=True),
        ),
    ]
