# Generated by Django 2.0.2 on 2019-05-28 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0015_auto_20190528_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotacionestarea',
            name='fecha_hora_anotacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 28, 12, 35, 6, 322597), null=True),
        ),
    ]