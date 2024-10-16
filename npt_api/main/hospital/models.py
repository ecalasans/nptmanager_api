from django.db import models
from main.abstract.models import AbstractModel, AbstractManager


# Create your models here.
class HospitalManager(AbstractManager):
    pass


class Hospital(AbstractModel):
    name = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitais'

    def __str__(self):
        return f"{self.name}({self.sigla})"
