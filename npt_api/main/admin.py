from django.contrib import admin

from main.hospital.models import Hospital
from main.patient.models import Paciente
from main.user.models import Medico

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Paciente)
admin.site.register(Medico)