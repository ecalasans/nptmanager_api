from django.contrib import admin
from main.hospital.models import Hospital
from main.medico.models import Medico

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Medico)

