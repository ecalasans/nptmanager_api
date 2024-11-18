# Generated by Django 5.1.2 on 2024-11-15 13:30

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("main_hospital", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Paciente",
            fields=[
                (
                    "public_id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("dn", models.DateField()),
                ("pnasc", models.IntegerField()),
                ("ignasc", models.CharField()),
                (
                    "cod_hospital",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="pacientes",
                        to="main_hospital.hospital",
                    ),
                ),
            ],
        ),
    ]
