# Generated by Django 2.0.2 on 2019-01-14 01:29

import apps.registration.models
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=apps.registration.models.elimina_imagen_cargada)),
                ('incentivo', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=6, null=True)),
                ('fecha_ingreso', models.DateField(default=django.utils.timezone.now)),
                ('fecha_salida', models.DateField(default=django.utils.timezone.now)),
                ('activo', models.BooleanField(default=False)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='registration.Area', verbose_name='Área')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
