import uuid
from django.db import models
from main.medico.models import Medico
from main.paciente.models import Paciente
from main.npt.models import Npt
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

# Create your models here.
class PrescricaoManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            instance  = self.get(public_id=public_id)
            return instance
        except ObjectDoesNotExist:
            raise Http404


class Prescricao(models.Model):
    public_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True,
    )
    cod_npt = models.ForeignKey(Npt, on_delete=models.DO_NOTHING, related_name='prescricao')
    cod_medico = models.ForeignKey(Medico, on_delete=models.DO_NOTHING, related_name='prescricao')
    peso = models.DecimalField(max_digits=5, decimal_places=1)
    volume = models.DecimalField(max_digits=4, decimal_places=1)
    vig = models.DecimalField(max_digits=2, decimal_places=1)
    aac = models.DecimalField(max_digits=2, decimal_places=1)
    lip = models.DecimalField(max_digits=2, decimal_places=1)
    ca = models.DecimalField(max_digits=2, decimal_places=1)
    na = models.DecimalField(max_digits=2, decimal_places=1)
    k = models.DecimalField(max_digits=2, decimal_places=1)
    p = models.DecimalField(max_digits=2, decimal_places=1)
    mg = models.DecimalField(max_digits=2, decimal_places=1)
    oligo = models.DecimalField(max_digits=2, decimal_places=1)
    vit = models.DecimalField(max_digits=2, decimal_places=1)
    data = models.DateTimeField(auto_now_add=True)

    objects = PrescricaoManager()

    class Meta:
        ordering = ('-data',)

    def __str__(self):
        return f'{self.data} - {self.cod_npt.cod_pac.nome}'

