# TODO:  Fazer o campo calculado da idade gestacional corrigida em semanas e dias
import datetime

from rest_framework import serializers

from main.hospital.models import Hospital
from main.leito.models import Leito
from main.paciente.models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    public_id = serializers.UUIDField(read_only=True, format='hex')
    created_at = serializers.DateTimeField(read_only=True, format='%d/%m/%Y %H:%M:%S')
    updated_at = serializers.DateTimeField(read_only=True, format='%d/%m/%Y %H:%M:%S')
    hospital = serializers.SlugRelatedField(
        slug_field='sigla',
        source='cod_hospital',
        read_only=True,
    )


    class Meta:
        model = Paciente
        fields = ['pk','public_id', 'nome', 'cod_hospital', 'hospital','cod_leito', 'dn', 'pnasc', 'ignasc', 'ignas_dias',
                  'created_at', 'updated_at', 'igc_atual']