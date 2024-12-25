from django.db import models

from CarMechanic.repairs.models import RepairSession


class Bus(models.Model):

    model = models.CharField(
        max_length=100,
    )

    number = models.CharField(
        max_length=20,
        unique=True,
        error_messages={'unique': 'Има бус с този номер!'},
    )

    km = models.IntegerField(
        null=True,
        blank=True,
    )


class Modifications(models.Model):

    session = models.ForeignKey(RepairSession, on_delete=models.CASCADE, related_name="modifications")

    repair = models.CharField(max_length=200)

    price = models.IntegerField()




