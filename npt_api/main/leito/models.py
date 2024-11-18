from django.db import models
from main.hospital.models import Hospital

# Create your models here.
class Leito(models.Model):
    leito = models.CharField(max_length=10)
    cod_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='leitos')

    def __str__(self):
        return f'{self.leito} - {self.cod_hospital.sigla}'
