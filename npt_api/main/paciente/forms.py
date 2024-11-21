from django import forms

from main.hospital.models import Hospital
from main.paciente.models import Paciente
from main.leito.models import Leito

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['cod_leito'].queryset = Leito.objects.filter(is_free=True).order_by('cod_hospital')
        self.fields['cod_hospital'].queryset = Hospital.objects.filter(is_active=True).order_by('nome')