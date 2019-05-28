# Generated by Django 2.0.2 on 2019-05-28 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0013_auto_20190409_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotacionestarea',
            name='fecha_hora_anotacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 28, 10, 46, 5, 624485), null=True),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='fecha_hora_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='fecha_hora_planificada',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]