from django.contrib import admin
from main.hospital.models import Hospital
from main.medico.models import Medico
from main.paciente.models import Paciente
from main.leito.models import Leito

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Leito)

