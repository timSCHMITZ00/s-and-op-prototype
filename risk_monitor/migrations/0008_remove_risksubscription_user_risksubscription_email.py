# Generated by Django 4.2.1 on 2023-05-15 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_monitor', '0007_riskmetric_setpoint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='risksubscription',
            name='user',
        ),
        migrations.AddField(
            model_name='risksubscription',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
