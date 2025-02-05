from rest_framework import serializers
from main.npt.models import Npt
from main.paciente.models import Paciente

class NptSerializer(serializers.ModelSerializer):
    public_id = serializers.UUIDField(read_only=True, format='hex')
    cod_pac = serializers.CharField(read_only=True)
    inicio = serializers.DateTimeField(read_only=True, format='%d/%m/%Y HH:mm:ss')
    fim = serializers.DateTimeField(read_only=True, format='%d/%m/%Y HH:mm:ss')

    class Meta:
        model = Npt
        fields = ['public_id', 'cod_pac', 'inicio', 'fim']