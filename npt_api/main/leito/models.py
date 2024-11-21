from django.db import models
from main.hospital.models import Hospital

# Create your models here.
class Leito(models.Model):
    leito = models.CharField(max_length=10)
    cod_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='leitos')
    is_free = models.BooleanField(default=True)

    def __str__(self):
        if self.is_free:
            return f'{self.leito} - {self.cod_hospital.sigla}(VAGO)'
        else:
            return f'{self.leito} - {self.cod_hospital.sigla}'
