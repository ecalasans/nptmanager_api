from django.db import models
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
import uuid

from main.paciente.models import Paciente
# Create your models here.
class NptManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            return Npt.objects.get(public_id=public_id)
        except ObjectDoesNotExist:
            raise Http404

    def filter_by_inicio(self, inicio):
        try:
            return Npt.objects.filter(inicio=inicio)
        except ObjectDoesNotExist:
            raise Http404


class Npt(models.Model):
    public_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True,
    )
    cod_pac = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING, related_name="npt")
    inicio = models.DateField()
    fim = models.DateField()

    objects = NptManager()

    class Meta:
        ordering = ("-inicio",)

    def __str__(self):
        return f"{self.cod_pac.nome} - {self.inicio}"
