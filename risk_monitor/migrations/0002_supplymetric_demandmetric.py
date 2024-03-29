# Generated by Django 4.2.1 on 2023-05-06 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risk_monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplyMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('unit', models.CharField(max_length=255)),
                ('value', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_monitor.risk')),
            ],
        ),
        migrations.CreateModel(
            name='DemandMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('unit', models.CharField(max_length=255)),
                ('value', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_monitor.risk')),
            ],
        ),
    ]
