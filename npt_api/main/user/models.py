import uuid

from django.db import models
from django.contrib.auth.models import User
from main.abstract.models import AbstractModel
from main.hospital.models import Hospital

# Create your models here.
class Medico(User):
    public_id = models.UUIDField(default=uuid.uuid4,
                                 editable=False,
                                 unique=True,
                                 db_index=True)
    crm = models.CharField(max_length=10, null=False)
    hospitais = models.ManyToManyField(to=Hospital,
                                       related_name='medicos',)

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {[i.sigla for i in self.hospitais.all()]}'

