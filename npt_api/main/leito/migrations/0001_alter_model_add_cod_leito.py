# Generated by Django 5.1.2 on 2024-11-18 00:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("main_hospital", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Leito",
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
                ("leito", models.CharField(max_length=10)),
                (
                    "cod_hospital",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="leitos",
                        to="main_hospital.hospital",
                    ),
                ),
            ],
        ),
    ]