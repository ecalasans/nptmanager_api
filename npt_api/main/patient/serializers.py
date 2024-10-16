from rest_framework import serializers

from main.patient.models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    public_id = serializers.UUIDField(
        read_only=True,
    )
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Paciente
        fields = ('public_id', 'nome', 'nasc', 'p_nasc', 'ig_nasc', 'created', 'updated')
