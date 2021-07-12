import datetime
from django.db import models

# Create your models here.


class CommonInfo1(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class CommonInfo2(CommonInfo1):
    diameter = models.PositiveIntegerField()
    color = models.CharField(max_length=100)
    star_system = models.ForeignKey("starsystem.StarSystem", on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True


class Galaxy(CommonInfo1):
    size_x = models.PositiveIntegerField()
    size_y = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Galaxies"


class StarSystem(CommonInfo1):
    position_x = models.PositiveIntegerField()
    position_y = models.PositiveIntegerField()
    galaxy = models.ForeignKey("starsystem.Galaxy", on_delete=models.SET_NULL, null=True)


class Star(CommonInfo2):
    pass


class Planet(CommonInfo2):
    live = models.BooleanField()
