# Generated by Django 5.1.2 on 2024-11-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_leito", "0001_alter_model_add_cod_leito"),
    ]

    operations = [
        migrations.AddField(
            model_name="leito",
            name="is_free",
            field=models.BooleanField(default=True),
        ),
    ]
