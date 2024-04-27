# Generated by Django 5.0.4 on 2024-04-21 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Engineer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("phone", models.CharField(max_length=16, unique=True)),
            ],
            options={
                "verbose_name": "Engineer",
                "verbose_name_plural": "Engineers",
            },
        ),
        migrations.CreateModel(
            name="EquipmentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20, unique=True)),
            ],
            options={
                "verbose_name": "Equipment Type",
                "verbose_name_plural": "Equipment Types",
            },
        ),
        migrations.CreateModel(
            name="Site",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10, unique=True)),
                ("address", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Site",
                "verbose_name_plural": "Sites",
            },
        ),
        migrations.CreateModel(
            name="Equipment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("serial_number", models.CharField(max_length=30, unique=True)),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.equipmenttype",
                    ),
                ),
            ],
            options={
                "verbose_name": "Equipment",
                "verbose_name_plural": "Equipments",
            },
        ),
    ]
