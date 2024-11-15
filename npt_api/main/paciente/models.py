import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404
from main.hospital.models import Hospital

# Create your models here.
class Paciente(models.Model):
    public_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    cod_hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING, related_name='pacientes')
    nome = models.CharField(max_length=100, null=False, blank=False)
    dn = models.DateField(null=False, blank=False)
    pnasc = models.IntegerField(null=False, blank=False)
    ignasc = models.CharField(null=False, blank=False)

    def __str__(self):
        return f'{self.nome} - {self.cod_hospital.sigla}'

