from django.db import models
import uuid

# Create your models here.
class Hospital(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,
                                 editable=False,
                                 db_index=True,
                                 unique=True)
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nome}({self.sigla})'
