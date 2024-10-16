from django.db import models
from main.abstract.models import AbstractModel, AbstractManager
from main.hospital.models import Hospital


# Create your models here.
class PatientManager(AbstractManager):
    pass

class Paciente(AbstractModel):
    cod_hospital = models.ForeignKey(
        to=Hospital,
        on_delete=models.CASCADE,
        related_name='pacientes',
    )
    nome = models.CharField(max_length=250)
    nasc = models.DateField()
    p_nasc = models.IntegerField()
    ig_nasc = models.IntegerField()

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return f'{self.nome} - {self.cod_hospital.sigla}'
