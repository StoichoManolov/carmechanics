from django.db import models

# Create your models here.


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

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

    date = models.DateField(null=True, blank=True)

    repair = models.CharField(max_length=200)

    price = models.IntegerField()



