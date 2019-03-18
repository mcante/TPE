# Generated by Django 2.0.2 on 2019-03-11 20:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tareas', '0002_auto_20190311_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareas',
            name='creado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rel_Tareas_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='replanificaciones',
            name='fecha_hora_replanificada',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='fecha_hora_completado',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='fecha_hora_planificada',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
