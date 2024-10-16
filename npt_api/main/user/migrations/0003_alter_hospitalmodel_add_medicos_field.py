# Generated by Django 5.1.1 on 2024-10-03 08:43

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_user", "0002_alter_model_name_medicomodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="medicomodel",
            name="public_id",
            field=models.UUIDField(
                db_index=True, default=uuid.uuid4, editable=False, unique=True
            ),
        ),
    ]