# Generated by Django 2.0.2 on 2019-03-28 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0007_auto_20190328_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotacionestarea',
            name='fecha_hora_anotacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 28, 11, 46, 55, 567519), null=True),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='fecha_hora_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 28, 11, 46, 55, 566518), null=True),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='fecha_hora_planificada',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 28, 11, 46, 55, 566518), null=True),
        ),
    ]
