from django.contrib import admin
import risk_monitor.models as models

# Register your models here.
admin.site.register(models.Risk)
admin.site.register(models.RiskEvent)
admin.site.register(models.RiskSubscription)
admin.site.register(models.RiskMetric)
admin.site.register(models.RiskMetricValue)