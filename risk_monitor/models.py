from django.db import models
from django.contrib.auth.models import User


class Risk(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    source = models.CharField(max_length=255, default='Network')
    category = models.CharField(max_length=255)
    score = models.CharField(max_length=255, default='Low')
    trend = models.CharField(max_length=255, default='Stable')

    def __str__(self):
        return self.name

class RiskEvent(models.Model):
    timestamp = models.DateTimeField()
    description = models.TextField()
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.risk}: {self.description}"
    
class RiskSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} subscribed to {self.risk}"
    
class RiskMetric(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    unit = models.CharField(max_length=255)
    setpoint = models.FloatField(default=0.0)
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    simulation_status = models.CharField(max_length=255, default='off')

    def __str__(self):
        return self.name
    
class RiskMetricValue(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField()
    risk_metric = models.ForeignKey(RiskMetric, on_delete=models.CASCADE)

    def __str__(self):
        return f"{RiskMetric.objects.get(name = self.risk_metric).name}: {self.value} {RiskMetric.objects.filter(name = self.risk_metric)[0].unit} at {self.timestamp}"
