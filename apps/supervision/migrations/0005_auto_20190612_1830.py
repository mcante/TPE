# Generated by Django 2.0.2 on 2019-06-13 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervision', '0004_auto_20190605_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='movimiento',
            field=models.IntegerField(unique=True),
        ),
    ]