import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404

from main.hospital.models import Hospital


class MedicoManager(BaseUserManager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            raise Http404

    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError('Precisa de um nome de usuário!')

        if email is None:
            raise TypeError('Precisa de um email!')

        if password is None:
            raise TypeError('Precisa de um password!')

        medico = self.model(username=username, email=self.normalize_email(email), **kwargs)
        medico.set_password(password)
        medico.save(using=self._db)

        return medico

class Medico(User):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    crm = models.CharField(max_length=255, unique=True, db_index=True)
    hospitais = models.ManyToManyField(
        to=Hospital,
        related_name='medicos',
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MedicoManager()

    class Meta:
        verbose_name = "medico"
        verbose_name_plural = "medicos"

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {[h.sigla for h in self.hospitais.all()]}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='medicos_groups'
    # )
    #
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='medicos_permissions'
    # )