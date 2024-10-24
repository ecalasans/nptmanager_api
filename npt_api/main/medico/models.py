import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
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

    def create_superuser(self, username, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **kwargs)

class Medico(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True)
    crm = models.CharField(max_length=255, unique=True, db_index=True)
    hospitais = models.ManyToManyField(
        to=Hospital,
        related_name='medicos',
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
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

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='medicos_groups',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='medicos_permissions',
        blank=True,
    )
