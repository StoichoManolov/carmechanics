from django.db import models

from CarMechanic.repairs.models import RepairSession


class Bus(models.Model):

    model = models.CharField(
        max_length=100,
        verbose_name='Модел:'
    )

    number = models.CharField(
        max_length=20,
        unique=True,
        error_messages={'unique': 'Има бус с този номер!'},
        verbose_name='Номер:'
    )

    km = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Километри:'
    )


class Modifications(models.Model):

    session = models.ForeignKey(RepairSession, on_delete=models.CASCADE, related_name="modifications")

    repair = models.CharField(max_length=200)

    price = models.IntegerField()




