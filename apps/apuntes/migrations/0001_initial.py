# Generated by Django 2.0.2 on 2019-01-27 23:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('nombre', models.CharField(max_length=150)),
                ('fecha', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('descripcion', models.TextField(blank=True, max_length=250, null=True, verbose_name='Descripción')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('titulo', models.CharField(max_length=150)),
                ('contenido', models.TextField(blank=True, null=True)),
                ('fecha', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('hora', models.TimeField(auto_now_add=True, null=True)),
                ('necesita_seguimiento', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_Nota_Categoria', to='apuntes.Categoria', verbose_name='Categoría')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
