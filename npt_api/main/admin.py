from django.contrib import admin
from main.hospital.models import Hospital
from main.medico.models import Medico
from main.paciente.models import Paciente
from main.leito.models import Leito
from main.paciente.forms import PacienteForm

#
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    listdisplay = ['nome', 'created_at']
    form = PacienteForm

    def delete_model(self, request, obj):
        obj.delete()

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()


admin.site.register(Hospital)
admin.site.register(Medico)
admin.site.register(Leito)

