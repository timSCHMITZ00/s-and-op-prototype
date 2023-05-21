# Generated by Django 4.2.1 on 2023-05-05 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KRI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('threshold', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RiskAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('agent_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RiskSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_monitor.risk')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RiskEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('description', models.TextField()),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_monitor.risk')),
                ('risk_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_monitor.riskagent')),
            ],
        ),
        migrations.CreateModel(
            name='KRIValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('value', models.FloatField()),
                ('kri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_monitor.kri')),
            ],
        ),
        migrations.AddField(
            model_name='kri',
            name='risk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_monitor.risk'),
        ),
    ]
