# Generated by Django 5.1.2 on 2025-03-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_npt", "0002_alter_fields_inicio_fim"),
    ]

    operations = [
        migrations.AlterField(
            model_name="npt",
            name="fim",
            field=models.DateField(blank=True),
        ),
    ]
