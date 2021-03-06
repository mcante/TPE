# Generated by Django 2.0.2 on 2019-01-15 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('evaluaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='aspectos_por_mejorar',
            field=models.TextField(blank=True, null=True, verbose_name='Aspectos a Mejorar'),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='evaluador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluacion_evaluador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='fecha',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='porcentaje_penalizacion',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='resultado',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
