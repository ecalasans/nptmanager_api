# Generated by Django 5.1.1 on 2024-10-16 20:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main_hospital", "0003_alter_nome_models"),
        ("main_patient", "0001_add_patient_model"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PatientModel",
            new_name="Paciente",
        ),
        migrations.AlterModelOptions(
            name="paciente",
            options={"verbose_name": "Paciente", "verbose_name_plural": "Pacientes"},
        ),
    ]