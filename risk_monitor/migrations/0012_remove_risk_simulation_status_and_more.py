# Generated by Django 4.2.1 on 2023-05-16 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_monitor', '0011_risk_simulation_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='risk',
            name='simulation_status',
        ),
        migrations.AddField(
            model_name='riskmetric',
            name='simulation_status',
            field=models.CharField(default='Off', max_length=255),
        ),
    ]
