# Generated by Django 4.2.1 on 2023-05-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_monitor', '0002_supplymetric_demandmetric'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk',
            name='score',
            field=models.CharField(default='Low', max_length=255),
        ),
        migrations.AddField(
            model_name='risk',
            name='trend',
            field=models.CharField(default='Stable', max_length=255),
        ),
    ]
