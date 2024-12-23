import uuid
import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404
from main.hospital.models import Hospital
from main.medico.models import Medico
from main.leito.models import Leito
import re

# Create your models here.
class PacienteManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            instance  = self.get(public_id=public_id)
            return instance
        except ObjectDoesNotExist:
            raise Http404


class Paciente(models.Model):
    public_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    cod_hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING, related_name='pacientes')
    cod_leito = models.ForeignKey(Leito, on_delete=models.DO_NOTHING, related_name='pacientes')
    nome = models.CharField(max_length=100, null=False, blank=False)
    dn = models.DateField(null=False, blank=False)
    pnasc = models.IntegerField(null=False, blank=False)
    ignasc = models.CharField(null=False, blank=False)
    added_by = models.ForeignKey(Medico, on_delete=models.DO_NOTHING, related_name='pacientes', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = PacienteManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.nome} - {self.cod_hospital.sigla}({self.cod_leito.leito})'

    @property
    def ignas_dias(self):
        regex = r'\d+'

        sem_d = [int(x) for x in re.findall(regex, self.ignasc)]

        return sem_d[0]*7 + sem_d[1]

    @property
    def igc_atual(self):
        hoje = datetime.date.today()

        diferenca = hoje - self.dn

        update_days = self.ignas_dias + diferenca.days

        semanas = int(update_days / 7)
        dias = update_days % 7

        return f'{semanas}sem{dias}d'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.cod_leito:
            leito = self.cod_leito
            leito.is_free = False
            leito.save()

    def delete(self, using = None, keep_parents = False):
        print(f"Deleting Paciente: {self}")
        if self.cod_leito:
            leito = self.cod_leito
            print(f"Leito before update: {leito}, is_free: {leito.is_free}")
            leito.is_free = True
            leito.save()
            print(f"Leito after update: {leito}, is_free: {leito.is_free}")

        super().delete(using=using, keep_parents=keep_parents)
        print(f"Paciente {self} deleted successfully")






