from django.db import models
from main.abstract.models import AbstractModel, AbstractManager
from main.patient.models import Paciente

# Create your models here.
class PrescricaoManager(AbstractManager):
    pass

class NPT(AbstractModel):
    paciente = models.ForeignKey(to=Paciente, on_delete=models.CASCADE, related_name='npt')
    fim = models.DateField()

    class Meta:
        verbose_name = 'npt'
        verbose_name_plural = 'npts'

    def __str__(self):
        return f'{self.paciente.nome} - {self.paciente.cod_hospital.sigla}({self.created})'

