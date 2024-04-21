from django.db import models


# Create your models here.
class Engineer(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    phone = models.CharField(max_length=16, unique=True, null=False)

    def __str__(self):
        return f"{self.name}, {self.phone}"

    class Meta:
        verbose_name = "Engineer"
        verbose_name_plural = "Engineers"


class EquipmentType(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Equipment Type"
        verbose_name_plural = "Equipment Types"


class Equipment(models.Model):
    serial_number = models.CharField(max_length=30, unique=True, null=False)
    type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.serial_number} ({self.type})"

    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"


class Site(models.Model):
    name = models.CharField(max_length=10, unique=True, null=False)
    address = models.CharField(max_length=50, unique=False, null=False)

    def __str__(self):
        return f"{self.name} ({self.address})"

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"
