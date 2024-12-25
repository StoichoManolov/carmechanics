from django.db import models
from django.utils.timezone import now

# Create your models here.


class RepairSession(models.Model):

    bus = models.ForeignKey('buses.Bus', on_delete=models.CASCADE, related_name="repair_sessions")
    km = models.IntegerField(blank=True, null=True)
    date = models.DateField(default=now)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)