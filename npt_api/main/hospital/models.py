from django.db import models
from main.abstract.models import AbstractModel, AbstractManager


# Create your models here.
class HospitalManager(AbstractManager):
    pass


class HospitalModel(AbstractModel):
    name = models.CharField(max_length=100)
