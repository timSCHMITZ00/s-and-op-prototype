# Generated by Django 4.2.1 on 2023-05-15 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('risk_monitor', '0008_remove_risksubscription_user_risksubscription_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='risksubscription',
            name='email',
        ),
        migrations.AddField(
            model_name='risksubscription',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
